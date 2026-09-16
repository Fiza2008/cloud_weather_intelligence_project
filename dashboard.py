import sqlite3
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "weather_intelligence.db"

st.set_page_config(page_title="Weather Intelligence", page_icon="🌦️", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.4rem;}
.hero {
    padding: 1.4rem 1.6rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #0f172a, #334155);
    color: white;
    margin-bottom: 1.2rem;
}
.hero h1 {margin: 0;}
.hero p {margin: .4rem 0 0; color: #cbd5e1;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🌦️ Weather Intelligence Platform</h1>
<p>Cloud-ready weather analytics powered by Python, SQL and Google Cloud</p>
</div>
""", unsafe_allow_html=True)

if not DB_PATH.exists():
    st.error("Database not found. Run `python -m src.pipeline` first.")
    st.stop()

@st.cache_data
def get_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM weather_observations", conn)
    conn.close()
    df["date"] = pd.to_datetime(df["date"])
    return df

df = get_data()

st.sidebar.header("🎛️ Filters")
city_options = sorted(df["city"].unique())
selected_cities = st.sidebar.multiselect("Cities", city_options, default=city_options[:5])

min_date = df["date"].min().date()
max_date = df["date"].max().date()
dates = st.sidebar.date_input("Date range", (min_date, max_date), min_value=min_date, max_value=max_date)

filtered = df[df["city"].isin(selected_cities)].copy()
if len(dates) == 2:
    filtered = filtered[
        (filtered["date"].dt.date >= dates[0]) &
        (filtered["date"].dt.date <= dates[1])
    ]

avg_temp = filtered["temperature_c"].mean() if len(filtered) else 0
avg_humidity = filtered["humidity_pct"].mean() if len(filtered) else 0
total_rain = filtered["precipitation_mm"].sum() if len(filtered) else 0
avg_wind = filtered["wind_speed_kmh"].mean() if len(filtered) else 0

a,b,c,d = st.columns(4)
a.metric("🌡️ Avg Temperature", f"{avg_temp:.1f} °C")
b.metric("💧 Avg Humidity", f"{avg_humidity:.1f}%")
c.metric("🌧️ Total Rainfall", f"{total_rain:.1f} mm")
d.metric("🌬️ Avg Wind", f"{avg_wind:.1f} km/h")

st.subheader("📈 Weather Trends")

daily = filtered.groupby("date", as_index=False).agg(
    temperature_c=("temperature_c","mean"),
    humidity_pct=("humidity_pct","mean"),
    precipitation_mm=("precipitation_mm","sum")
)

col1,col2 = st.columns(2)
with col1:
    fig = px.line(daily, x="date", y="temperature_c", markers=True,
                  title="Average Temperature Trend",
                  labels={"temperature_c":"Temperature (°C)","date":"Date"})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(daily, x="date", y="humidity_pct",
                  title="Average Humidity Trend",
                  labels={"humidity_pct":"Humidity (%)","date":"Date"})
    st.plotly_chart(fig, use_container_width=True)

col3,col4 = st.columns(2)
with col3:
    city_temp = filtered.groupby("city", as_index=False)["temperature_c"].mean()
    fig = px.bar(city_temp.sort_values("temperature_c"),
                 x="temperature_c", y="city", orientation="h",
                 title="Average Temperature by City",
                 labels={"temperature_c":"Temperature (°C)","city":"City"})
    st.plotly_chart(fig, use_container_width=True)

with col4:
    city_rain = filtered.groupby("city", as_index=False)["precipitation_mm"].sum()
    fig = px.bar(city_rain.sort_values("precipitation_mm"),
                 x="precipitation_mm", y="city", orientation="h",
                 title="Rainfall by City",
                 labels={"precipitation_mm":"Rainfall (mm)","city":"City"})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("🏙️ City Summary")
summary = filtered.groupby(["city","state"], as_index=False).agg(
    avg_temperature_c=("temperature_c","mean"),
    avg_humidity_pct=("humidity_pct","mean"),
    avg_wind_kmh=("wind_speed_kmh","mean"),
    total_rainfall_mm=("precipitation_mm","sum"),
    observations=("city","size")
).round(2)

st.dataframe(summary, use_container_width=True, hide_index=True)

st.caption("Portfolio project. Sample data is included for offline execution; optional GCS and BigQuery modules support Google Cloud deployment.")

import pandas as pd

REQUIRED_COLUMNS = [
    "date","city","state","temperature_c","humidity_pct",
    "wind_speed_kmh","precipitation_mm","condition"
]

def validate(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    numeric = ["temperature_c","humidity_pct","wind_speed_kmh","precipitation_mm"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date","city"] + numeric)
    df = df.drop_duplicates(subset=["date","city"])

    df = df[(df["humidity_pct"] >= 0) & (df["humidity_pct"] <= 100)]
    df = df[df["wind_speed_kmh"] >= 0]
    df = df[df["precipitation_mm"] >= 0]

    return df

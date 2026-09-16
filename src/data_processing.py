import pandas as pd

def transform(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.month_name()
    df["day_name"] = df["date"].dt.day_name()

    df["temperature_f"] = (df["temperature_c"] * 9/5 + 32).round(2)
    df["heat_index_proxy"] = (
        df["temperature_c"] + 0.05 * df["humidity_pct"]
    ).round(2)

    return df

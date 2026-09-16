import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path(__file__).resolve().parents[1] / "database" / "weather_intelligence.db"

def load(df):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("weather_observations", conn, if_exists="replace", index=False)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_weather_city ON weather_observations(city)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_weather_date ON weather_observations(date)")
    conn.commit()
    conn.close()
    return DB_PATH

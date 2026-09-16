from pathlib import Path
import pandas as pd

from src.data_validation import validate
from src.data_processing import transform
from src.database import load as load_sqlite

BASE_DIR = Path(__file__).resolve().parents[1]

def run_sample_pipeline():
    raw_path = BASE_DIR / "data" / "raw" / "weather_sample.csv"
    processed_path = BASE_DIR / "data" / "processed" / "weather_processed.csv"

    print("Extracting weather data...")
    raw = pd.read_csv(raw_path)
    print(f"Rows extracted: {len(raw):,}")

    print("Validating and transforming data...")
    clean = validate(raw)
    processed = transform(clean)

    processed.to_csv(processed_path, index=False)

    print("Loading local analytics database...")
    db = load_sqlite(processed)

    print(f"Processed rows: {len(processed):,}")
    print(f"SQLite database: {db}")
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_sample_pipeline()

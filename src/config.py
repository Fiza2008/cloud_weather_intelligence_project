import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "")
GCS_BUCKET = os.getenv("GCS_BUCKET", "")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET", "weather_intelligence")
BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE", "weather_observations")

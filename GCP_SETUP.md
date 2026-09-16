# Google Cloud Setup

The project works locally with the included sample data. Google Cloud integration is optional.

## Authenticate

```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

Enable Cloud Storage and BigQuery APIs in your Google Cloud project.

## Create a Cloud Storage bucket

```bash
gcloud storage buckets create gs://YOUR_BUCKET_NAME --location=asia-south1
```

## Create the BigQuery dataset

```bash
bq --location=asia-south1 mk -d YOUR_PROJECT_ID:weather_intelligence
```

## Upload processed data to GCS

```python
from src.gcp_storage import upload_to_gcs

upload_to_gcs(
    "data/processed/weather_processed.csv",
    "YOUR_BUCKET_NAME",
    "processed/weather_processed.csv"
)
```

## Load processed data to BigQuery

```python
from src.bigquery_loader import load_to_bigquery
import pandas as pd

df = pd.read_csv("data/processed/weather_processed.csv")

load_to_bigquery(
    df,
    "YOUR_PROJECT_ID",
    "weather_intelligence",
    "weather_observations"
)
```

Never commit `.env`, API keys, or service-account private keys.

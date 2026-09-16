# 🌦️ Cloud Weather Intelligence Platform

> A cloud-ready weather data engineering project using Python, ETL, SQL, Google Cloud Storage, BigQuery and Streamlit.

## 🌐 Web Application

This project includes an interactive **Weather Intelligence Dashboard**.

```bash
pip install -r requirements.txt
python -m src.pipeline
streamlit run dashboard.py
```

Then open:

```text
http://localhost:8501
```

The website provides:

- 🌡️ Average temperature
- 💧 Average humidity
- 🌧️ Rainfall
- 🌬️ Wind speed
- 📈 Temperature and humidity trends
- 🏙️ City comparison
- 📅 Date filters
- 🔎 City filters
- 📋 City-level summary

## ☁️ Google Cloud Architecture

```text
Weather API / Sample Data
          ↓
      Python ETL
          ↓
 Data Validation & Cleaning
          ↓
   ┌──────┴───────┐
   ↓              ↓
Google Cloud    BigQuery
  Storage      Data Warehouse
   ↓              ↓
Raw/Processed   SQL Analytics
       \          /
        \        /
       Streamlit
       Dashboard
```

### GCP services

| Service | Purpose |
|---|---|
| Google Cloud Storage | Raw and processed object storage |
| BigQuery | Cloud data warehouse and SQL analytics |
| Cloud IAM | Access control |
| gcloud CLI | Cloud management |

See `GCP_SETUP.md` for setup.

## 🔄 ETL Pipeline

### Extract
Reads included sample weather data. `src/api_client.py` can optionally retrieve current weather from a weather API.

### Transform
- Removes duplicates
- Validates numeric ranges
- Converts dates
- Creates year/month/day fields
- Calculates Fahrenheit temperature
- Creates a simple analytical heat-index proxy

### Load
Stores processed data locally in:

```text
database/weather_intelligence.db
```

The same data can optionally be uploaded to GCS and loaded into BigQuery.

## 📊 SQL Analytics

`sql/weather_analysis.sql` includes:

- Average temperature by city
- Average humidity by city
- Monthly rainfall
- Hottest observations
- Wind analysis

`sql/data_quality.sql` includes null, range and duplicate checks.

## 📁 Project Structure

```text
cloud_weather_intelligence/
│
├── data/
│   ├── raw/weather_sample.csv
│   └── processed/weather_processed.csv
├── database/weather_intelligence.db
├── src/
│   ├── api_client.py
│   ├── config.py
│   ├── data_processing.py
│   ├── data_validation.py
│   ├── database.py
│   ├── gcp_storage.py
│   ├── bigquery_loader.py
│   └── pipeline.py
├── sql/
│   ├── weather_analysis.sql
│   └── data_quality.sql
├── tests/test_pipeline.py
├── dashboard.py
├── GCP_SETUP.md
├── .env.example
├── requirements.txt
└── README.md
```

## 🛠️ Technologies

Python • Pandas • REST API • SQL • Google Cloud Storage • BigQuery • Streamlit • Plotly • Pytest • Git/GitHub

## ▶️ Run

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run ETL:

```bash
python -m src.pipeline
```

Start website:

```bash
streamlit run dashboard.py
```

Run tests:

```bash
pytest
```


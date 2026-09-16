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

## 🎤 Interview Explanation

> I built a cloud-ready weather intelligence platform using Python and Pandas. The ETL pipeline extracts weather observations, validates and transforms them, and stores the processed data for analytics. I integrated Google Cloud Storage as the object-storage layer and BigQuery as the cloud data warehouse, while a Streamlit dashboard provides interactive analysis.

### Why BigQuery?

BigQuery provides a serverless analytical warehouse where large datasets can be queried using SQL.

### Why Cloud Storage?

Cloud Storage provides object storage for raw and processed files and separates storage from analytics.

### ETL vs ELT

ETL transforms data before loading it. ELT loads data first and performs transformations in the target platform.

## 📄 Resume Version

**Cloud Weather Intelligence Platform | Python, GCP, BigQuery, Cloud Storage, SQL, Streamlit**

- Built a cloud-ready ETL pipeline using Python and Pandas to validate, transform and analyze **1,800+ weather observations** across multiple cities.
- Integrated **Google Cloud Storage and BigQuery** as cloud storage and analytical warehouse layers, with SQL queries for weather trends and data-quality analysis.
- Developed an interactive **Streamlit web dashboard** with filters, KPIs and Plotly visualizations for temperature, humidity, rainfall and wind analytics.

## 🔮 Future Improvements

- Cloud Scheduler
- Cloud Functions
- BigQuery partitioning and clustering
- Incremental loading
- Data-quality monitoring
- Looker Studio
- Cloud Composer / Airflow
- Weather forecasting ML
- Docker and CI/CD

## ⭐ Author

**Fiza Naz Shaik**

B.Tech Computer Science & Engineering — AI/ML  
VIT-AP

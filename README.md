# 🌦️ Weather Data ETL Pipeline

This is a Python-based ETL (Extract, Transform, Load) pipeline that fetches real-time weather data from the OpenWeatherMap API, transforms it for trend analysis, and loads the output into S3.

## 🔧 Features
- Extract current weather data using OpenWeatherMap API
- Transform for daily trend analysis
- `weather_data.csv`: Raw weather records
- S3 path: `s3://your-s3-bucket/weather_data/weather_data.csv`
- BigQuery Table: `your_dataset.weather_data`

## 🛠️ Tools Used
- Google BigQuery
- google-cloud-bigquery
from dotenv import load_dotenv
import os 

load_dotenv()


LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
GCP_PROJECT = os.getenv("GCP_PROJECT")
BQ_DATASET = os.getenv("BQ_DATASET")
BQ_TABLE = os.getenv("BQ_TABLE")

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

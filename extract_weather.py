import requests
from config import WEATHER_API_URL, LATITUDE, LONGITUDE


def extract_weather():
    params = {
        'latitude': LATITUDE,
        'longitude': LONGITUDE,
        'current_weather': 'true'
    }
    response = requests.get(WEATHER_API_URL, params=params)

    # data = response.json()
    # print("📦 Extracted Data:", data)
    response.raise_for_status()
    return response.json()


# extract_weather()

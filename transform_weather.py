import pandas as pd
from datetime import datetime


def transform_weather(raw_data):
    current = raw_data['current_weather']
    weather = {
        'temperature_celsius': current['temperature'],
        'windspeed': current['windspeed'],
        'weathercode': current.get('weathercode', None),
        'timestamp': datetime.utcnow()
    }

    df = pd.DataFrame([weather])
    df.dropna(inplace=True)
    df.dropna(inplace=True)
    print(f"This is the DataFrmae: {df}")
    return df

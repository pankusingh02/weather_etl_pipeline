from extract_weather import extract_weather
from transform_weather import transform_weather
from load_to_bigquery import load_to_bigquery

def main():
    raw_data=extract_weather()
    df= transform_weather(raw_data)
    load_to_bigquery(df)


if __name__=='main':
    main()
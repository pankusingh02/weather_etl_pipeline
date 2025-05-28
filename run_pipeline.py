from extract_weather import extract_weather
from transform_weather import transform_weather
from load_to_bigquery import load_to_bigquery

def main():
   print("🔄 Extracting weather data...")
   raw_data = extract_weather()
   print("✅ Extracted:", raw_data)

   print("🧪 Transforming data...")
   df = transform_weather(raw_data)
   print("✅ Transformed dataframe:\n", df)

   print("🚀 Loading into BigQuery...")
   load_to_bigquery(df)
   print("✅ Done.")

if __name__=='__main__':
    main()
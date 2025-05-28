from google.cloud import bigquery
from config import GCP_PROJECT, BQ_DATASET, BQ_TABLE
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-creds.json"


def load_to_bigquery(df):
    client = bigquery.Client()
    print("✅ Authenticated as:", client.project)
    table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{BQ_TABLE}"
    job = client.load_table_from_dataframe(df, table_id)
    job_result=job.result()
    print(job_result)
    print(f'loaded {len(df)} rows to {table_id}')

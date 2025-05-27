from google.cloud import bigquery
from config import GCP_PROJECT, BQ_DATASET, BQ_TABLE


def load_to_bigquery(df):
    client = bigquery.client()
    table_id = f"{GCP_PROJECT},{BQ_DATASET},{BQ_TABLE}"
    job = client.load_table_from_dataframe(df, table_id)
    job_result=job.result()
    print(job_result)
    print(f'loaded {len(df)} rows to {table_id}')

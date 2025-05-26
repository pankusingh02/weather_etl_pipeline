FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pandas requests boto3 psycopg2-binary python-dotenv

CMD ["python", "run_pipeline.py"]
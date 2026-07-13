FROM apache/airflow:3.0.4-python3.11

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && apt-get clean

USER airflow

RUN pip install --no-cache-dir \
    duckdb \
    duckdb-engine \
    pandas \
    pyarrow \
    boto3 \
    minio \
    dbt-duckdb \
    great-expectations
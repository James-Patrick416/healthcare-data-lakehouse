# ------------------------------------------------------------------------------
# Healthcare Data Lakehouse
# Custom Airflow Image
#
# Extends the official Apache Airflow image with project dependencies.
# ------------------------------------------------------------------------------

# Official Airflow image
FROM apache/airflow:3.3.0-python3.11

# Switch to root to install system packages
USER root

# Install system packages required by Python libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Return to the airflow user for security
USER airflow

# Copy dependency list into the image
COPY docker/airflow/requirements.txt /requirements.txt

# Install project-specific Python packages
RUN pip install --no-cache-dir -r /requirements.txt
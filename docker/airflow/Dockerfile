# -------------------------------------------------------------------
# Custom Airflow Image
#
# Purpose:
# Extends the official Airflow image with project-specific
# Python dependencies needed by our Healthcare Data Lakehouse.
# -------------------------------------------------------------------

# Use a fixed Airflow version for reproducible builds.
FROM apache/airflow:3.0.4-python3.11

# Switch to root so we can install system packages.
USER root

# Install only the system packages we actually need.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user.
# Containers should not run as root unless absolutely necessary.
USER airflow

# Copy Python dependencies into the image.
COPY docker/airflow/requirements.txt /requirements.txt

# Install Python packages.
#
# --no-cache-dir keeps the image smaller by discarding pip's cache.
RUN pip install --no-cache-dir -r /requirements.txt
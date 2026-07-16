#!/bin/sh

# ----------------------------------------------------------
# Create the Healthcare Data Lakehouse bucket in MinIO.
# This script is idempotent, so it is safe to run multiple
# times.
# ----------------------------------------------------------

set -e

# Configure the MinIO client
mc alias set local http://minio:9000 minioadmin minioadmin

# Create the bucket if it does not already exist
mc mb --ignore-existing local/healthcare-lakehouse

echo "Bucket healthcare-lakehouse is ready."
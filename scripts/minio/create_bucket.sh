#!/bin/sh

set -e

# Configure MinIO client
mc alias set local http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD}

# Create the bucket
mc mb --ignore-existing local/${MINIO_BUCKET}

# Create Bronze layer prefixes
touch /tmp/.keep

mc cp /tmp/.keep local/${MINIO_BUCKET}/bronze/encounters/.keep
mc cp /tmp/.keep local/${MINIO_BUCKET}/bronze/patients/.keep
mc cp /tmp/.keep local/${MINIO_BUCKET}/bronze/providers/.keep

echo "Bronze layer initialized."
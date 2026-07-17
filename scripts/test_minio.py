from healthcare_data_lakehouse.storage.minio_client import MinIOClient

client = MinIOClient()

if client.bucket_exists():
    print("✅ Connected to MinIO")
    print(f"Bucket '{client.bucket}' exists.")
else:
    print("❌ Bucket does not exist.")

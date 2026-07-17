from minio import Minio

from healthcare_data_lakehouse.ingestion.config import (
    MINIO_ACCESS_KEY,
    MINIO_BUCKET,
    MINIO_ENDPOINT,
    MINIO_SECRET_KEY,
)


class MinIOClient:
    """
    Wrapper around the MinIO Python SDK.

    All object storage interactions should go through this class.
    """

    def __init__(self) -> None:
        self.bucket = MINIO_BUCKET

        self.client = Minio(
            endpoint=MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False,
        )

    def bucket_exists(self) -> bool:
        """Return True if the configured bucket exists."""
        return self.client.bucket_exists(self.bucket)

    def upload_file(self, object_name: str, file_path: str) -> None:
        """Upload a local file into the configured bucket."""
        self.client.fput_object(
            bucket_name=self.bucket,
            object_name=object_name,
            file_path=file_path,
        )

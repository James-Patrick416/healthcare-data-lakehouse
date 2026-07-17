"""
Bronze layer ingestion.

Reads raw CSV data and writes it as Parquet files.
"""

from pathlib import Path

import pandas as pd

from healthcare_data_lakehouse.ingestion.readers import read_csv
from healthcare_data_lakehouse.storage.minio_client import MinIOClient


def csv_to_parquet(csv_path: Path, output_path: Path) -> None:
    """
    Convert a CSV file into a Parquet file.

    Parameters
    ----------
    csv_path : Path
        Source CSV file.
    output_path : Path
        Destination Parquet file.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df: pd.DataFrame = read_csv(csv_path)

    df.to_parquet(
        output_path,
        engine="pyarrow",
        compression="snappy",
        index=False,
    )

    # Upload Bronze dataset to MinIO
    client = MinIOClient()

    client.upload_file(
        object_name="bronze/patients/patients.parquet",
        file_path=str(output_path),
    )

    print("Uploaded Bronze dataset to MinIO.")
    print(f"Created {output_path}")

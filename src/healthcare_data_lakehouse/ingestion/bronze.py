"""
Bronze layer ingestion.

Reads raw CSV data and writes it as Parquet files.
"""

from pathlib import Path

import pandas as pd

from healthcare_data_lakehouse.ingestion.readers import read_csv


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

    print(f"Created {output_path}")

from healthcare_data_lakehouse.ingestion.bronze import csv_to_parquet
from healthcare_data_lakehouse.ingestion.config import (
    BRONZE_LOCAL_DIR,
    PATIENTS_CSV,
)

output = BRONZE_LOCAL_DIR / "patients.parquet"

csv_to_parquet(PATIENTS_CSV, output)

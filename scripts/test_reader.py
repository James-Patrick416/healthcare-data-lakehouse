from healthcare_data_lakehouse.ingestion.config import PATIENTS_CSV
from healthcare_data_lakehouse.ingestion.readers import read_csv

df = read_csv(PATIENTS_CSV)

print(df.head())
print(f"\nRows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

from pathlib import Path

import pandas as pd

PARQUET_FILE = Path("data/bronze/patients.parquet")

df = pd.read_parquet(PARQUET_FILE)

print("=" * 80)
print(df.head())
print("=" * 80)
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print("\nSchema:")
print(df.dtypes)

"""
Configuration for Bronze ingestion.

All filesystem paths are defined here so they are managed in one place.
"""

from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Raw source data
SAMPLE_DATA_DIR = PROJECT_ROOT / "data" / "sample"

# Bronze landing zone before upload to MinIO
BRONZE_LOCAL_DIR = PROJECT_ROOT / "data" / "bronze"

# Core healthcare datasets
PATIENTS_CSV = SAMPLE_DATA_DIR / "patients.csv"
ENCOUNTERS_CSV = SAMPLE_DATA_DIR / "encounters.csv"
PROVIDERS_CSV = SAMPLE_DATA_DIR / "providers.csv"

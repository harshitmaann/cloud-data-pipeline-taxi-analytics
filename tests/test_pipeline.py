from pathlib import Path

def test_processed_parquet_exists():
    assert Path("data/processed/taxis_clean.parquet").exists()

# Cloud Data Pipeline + Analytics (Taxi Data)

End-to-end data pipeline that downloads a public taxi dataset, transforms it into analytics-ready Parquet, runs SQL analytics with DuckDB, and generates reports + charts. Designed to be reproducible and CI-tested.

## Tech
Python, Pandas, DuckDB, Parquet (PyArrow), Matplotlib, GitHub Actions

## Project structure
- `src/pipeline/` extract + transform scripts
- `src/analysis/` analytics + charts
- `data/raw/` raw input (gitignored)
- `data/processed/` curated parquet (gitignored)
- `reports/` outputs (csv + charts; gitignored by default)
- `.github/workflows/` CI pipeline

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make run
```

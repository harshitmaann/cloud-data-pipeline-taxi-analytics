.PHONY: install extract transform analyze run test clean

install:
	pip install -r requirements.txt

extract:
	python -m src.pipeline.extract

transform:
	python -m src.pipeline.transform

analyze:
	python -m src.analysis.analyze

run: extract transform analyze

test:
	pytest -q

clean:
	rm -rf data/raw/* data/processed/* reports/analytics.duckdb reports/*.csv reports/figures/*

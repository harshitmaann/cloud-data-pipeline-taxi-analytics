import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/taxis.csv")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_PARQUET = OUT_DIR / "taxis_clean.parquet"

def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Missing raw file: {RAW_FILE}. Run extract first.")

    df = pd.read_csv(RAW_FILE)

    df["pickup"] = pd.to_datetime(df["pickup"])
    df["dropoff"] = pd.to_datetime(df["dropoff"])

    df["trip_minutes"] = (df["dropoff"] - df["pickup"]).dt.total_seconds() / 60.0
    df["pickup_date"] = df["pickup"].dt.date
    df["pickup_hour"] = df["pickup"].dt.hour
    df["pickup_weekday"] = df["pickup"].dt.day_name()

    df = df[df["trip_minutes"].between(1, 180)]
    df = df[df["fare"].between(1, 500)]

    df.to_parquet(OUT_PARQUET, index=False)
    print(f"[transform] Wrote: {OUT_PARQUET} rows={len(df)}")

if __name__ == "__main__":
    main()

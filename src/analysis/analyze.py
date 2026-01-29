import duckdb
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/processed/taxis_clean.parquet")
REPORTS = Path("reports")
FIGS = Path("reports/figures")
REPORTS.mkdir(exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError("Missing processed parquet. Run transform first.")

    con = duckdb.connect(database=str(REPORTS / "analytics.duckdb"))
    con.execute(f"CREATE OR REPLACE VIEW trips AS SELECT * FROM read_parquet('{DATA}')")

    kpis = con.execute("""
        SELECT
            COUNT(*) AS trips,
            AVG(fare) AS avg_fare,
            AVG(trip_minutes) AS avg_trip_minutes,
            AVG(passengers) AS avg_passengers
        FROM trips
    """).df()
    kpis.to_csv(REPORTS / "kpis.csv", index=False)
    print("[analyze] Wrote reports/kpis.csv")

    by_hour = con.execute("""
        SELECT pickup_hour, COUNT(*) AS trips
        FROM trips
        GROUP BY 1
        ORDER BY 1
    """).df()

    plt.figure()
    plt.plot(by_hour["pickup_hour"], by_hour["trips"])
    plt.title("Trips by Pickup Hour")
    plt.xlabel("Hour")
    plt.ylabel("Trips")
    plt.savefig(FIGS / "trips_by_hour.png", dpi=200, bbox_inches="tight")
    print("[analyze] Wrote reports/figures/trips_by_hour.png")

    by_weekday = con.execute("""
        SELECT pickup_weekday, AVG(fare) AS avg_fare
        FROM trips
        GROUP BY 1
        ORDER BY avg_fare DESC
    """).df()
    by_weekday.to_csv(REPORTS / "avg_fare_by_weekday.csv", index=False)
    print("[analyze] Wrote reports/avg_fare_by_weekday.csv")

if __name__ == "__main__":
    main()

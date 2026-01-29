import urllib.request
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
OUTFILE = RAW_DIR / "taxis.csv"

def main(url: str = DEFAULT_URL) -> None:
    if OUTFILE.exists():
        print(f"[extract] Already exists: {OUTFILE}")
        return
    print(f"[extract] Downloading from: {url}")
    urllib.request.urlretrieve(url, OUTFILE)
    print(f"[extract] Saved: {OUTFILE}")

if __name__ == "__main__":
    main()

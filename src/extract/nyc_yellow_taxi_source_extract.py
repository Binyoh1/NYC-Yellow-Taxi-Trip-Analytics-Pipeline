import requests
from pathlib import Path

# ensure parent data diretory exists else create
DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)

# Setup
BASE_URL = "https://d37ci6vzurychx.cloudfront.net"
YEARS = [year for year in range(2018, 2026)]

def fetch_yellow_taxi_data(years: list[int]) -> None:
    """Fetches yellow taxi data for each given year and saves it to data directory"""    
    for year in years:
        for month in range(1, 13):
            yellow_taxi_url = f"{BASE_URL}/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
            filename = f"yellow_tripdata_{year}-{month:02d}.parquet"
            file_path = DATA_DIR / f"{year}" / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            try:                
                response = requests.get(yellow_taxi_url, stream=True, timeout=10)
                response.raise_for_status()
                if not file_path.exists():
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                        print(f"Downloaded {filename}")
                else:
                    print(f"{filename} already exists")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {yellow_taxi_url}: {e}")
                
if __name__ == "__main__":
    fetch_yellow_taxi_data(YEARS)
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# API Configuration
API_BASE_URL = "https://dummyjson.com/products"
API_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

# Data Paths
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
LOGS_DIR = BASE_DIR / "logs"

# Ensure directories exist
for folder in [RAW_DATA_DIR, PROCESSED_DATA_DIR, LOGS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# File Names
RAW_FILENAME = "products_raw.json"
PROCESSED_JSON_FILENAME = "products_processed.json"
PROCESSED_CSV_FILENAME = "products_processed.csv"

# ETL Settings
LOG_FILE = LOGS_DIR / "etl.log"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

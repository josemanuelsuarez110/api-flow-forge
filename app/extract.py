import requests
import json
from app.config import API_BASE_URL, API_TIMEOUT, MAX_RETRIES, RAW_DATA_DIR, RAW_FILENAME
from app.utils import get_logger

logger = get_logger("extract")

def fetch_products(limit=10, skip=0):
    """Fetches a batch of products from the API."""
    params = {
        "limit": limit,
        "skip": skip
    }
    
    try:
        logger.info(f"Fetching products skip={skip}, limit={limit}...")
        response = requests.get(
            API_BASE_URL,
            params=params,
            timeout=API_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching products: {e}")
        return None

def extract_all_products(max_records=100):
    """Orchestrates extraction of all products with pagination."""
    all_products = []
    skip = 0
    batch_size = 30
    
    while len(all_products) < max_records:
        data = fetch_products(limit=batch_size, skip=skip)
        
        if not data or "products" not in data:
            logger.warning("No more data received or unexpected format.")
            break
            
        batch = data["products"]
        if not batch:
            logger.info("Empty batch received. End of data.")
            break
            
        all_products.extend(batch)
        logger.info(f"Extracted {len(batch)} records. Total: {len(all_products)}")
        
        skip += batch_size
        
        # Check if we've reached the end
        if skip >= data.get("total", 0):
            break
            
    # Cache raw data
    raw_path = RAW_DATA_DIR / RAW_FILENAME
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=4)
        
    logger.info(f"Raw data saved to {raw_path}")
    return all_products

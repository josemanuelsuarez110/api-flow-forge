import pandas as pd
import json
from app.config import PROCESSED_DATA_DIR, PROCESSED_JSON_FILENAME, PROCESSED_CSV_FILENAME
from app.utils import get_logger

logger = get_logger("load")

def load_data_to_json(data):
    """Saves the data to a JSON file."""
    output_path = PROCESSED_DATA_DIR / PROCESSED_JSON_FILENAME
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data saved to JSON: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error saving to JSON: {e}")
        return False

def load_data_to_csv(data):
    """Saves the data to a CSV file using pandas."""
    output_path = PROCESSED_DATA_DIR / PROCESSED_CSV_FILENAME
    
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        logger.info(f"Data saved to CSV: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error saving to CSV: {e}")
        return False

def load_summary(total_extracted, total_transformed, total_loaded, execution_time):
    """Prints a summary of the ETL process."""
    logger.info("=" * 50)
    logger.info("ETL PROCESS SUMMARY")
    logger.info("=" * 50)
    logger.info(f"Extracted records:   {total_extracted}")
    logger.info(f"Transformed records: {total_transformed}")
    logger.info(f"Loaded records:      {total_loaded}")
    logger.info(f"Execution time:      {execution_time:.2f} seconds")
    logger.info("=" * 50)

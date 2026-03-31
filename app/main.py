import time
from app.utils import setup_logging
from app.extract import extract_all_products
from app.transform import transform_all_products
from app.load import load_data_to_json, load_data_to_csv, load_summary

def run_etl():
    """Main function to run the ETL pipeline."""
    logger = setup_logging()
    
    start_time = time.time()
    
    logger.info("Starting API Flow Forge ETL Pipeline...")
    
    # 1. Extract
    raw_data = extract_all_products(max_records=100) # Full dataset for portfolio
    
    if not raw_data:
        logger.error("Extraction failed. Stopping ETL.")
        return
        
    # 2. Transform
    processed_data = transform_all_products(raw_data)
    
    if not processed_data:
        logger.error("Transformation failed. Stopping ETL.")
        return
        
    # 3. Load
    json_success = load_data_to_json(processed_data)
    csv_success = load_data_to_csv(processed_data)
    
    # 4. Summary
    end_time = time.time()
    execution_time = end_time - start_time
    
    load_summary(
        total_extracted=len(raw_data),
        total_transformed=len(processed_data),
        total_loaded=len(processed_data) if (json_success and csv_success) else 0,
        execution_time=execution_time
    )

if __name__ == "__main__":
    run_etl()

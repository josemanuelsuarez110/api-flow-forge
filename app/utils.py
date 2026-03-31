import logging
import sys
from app.config import LOG_FILE, LOG_LEVEL

def setup_logging():
    """Sets up the logging configuration."""
    
    # Configure logging format
    log_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Create logger
    logger = logging.getLogger("api_flow_forge")
    logger.setLevel(LOG_LEVEL)
    
    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(logging.Formatter(log_format, date_format))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format, date_format))
    
    # Add handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

def get_logger(module_name):
    """Returns a logger for a specific module."""
    return logging.getLogger(f"api_flow_forge.{module_name}")

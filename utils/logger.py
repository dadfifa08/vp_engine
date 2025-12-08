import logging
import os
from datetime import datetime

# Directory for logs
LOG_DIR = "logs"

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str):
    """Creates a logger with rotating daily log files"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if logger is reused
    if logger.handlers:
        return logger

    log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
    filepath = os.path.join(LOG_DIR, log_filename)

    handler = logging.FileHandler(filepath)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

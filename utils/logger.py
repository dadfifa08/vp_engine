import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = \"logs\"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_path = os.path.join(LOG_DIR, f\"{name}.log\")

    handler = RotatingFileHandler(
        log_path,
        maxBytes=5_000_000,
        backupCount=3,
        encoding=\"utf-8\"
    )

    formatter = logging.Formatter(
        '%(asctime)s — %(name)s — %(levelname)s — %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("vp_engine")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        file_handler = RotatingFileHandler(
            "vp_engine.log",
            maxBytes=2_000_000,
            backupCount=3
        )
        file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger

log = setup_logger()

from utils.logger import setup_logger
logger = setup_logger(\"analytics\")

class Analytics:
    def log_event(self, event: str, payload=None):
        logger.info(f\"{event} — {payload}\")

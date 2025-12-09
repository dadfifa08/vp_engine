import threading
import time
from utils.logger import setup_logger

logger = setup_logger("analytics")

class AnalyticsCollector:
    def __init__(self):
        self.running = True

    def start(self):
        t = threading.Thread(target=self.loop, daemon=True)
        t.start()

    def loop(self):
        while self.running:
            logger.info("Collecting analytics…")
            time.sleep(60)

from utils.logger import log
import time

class TrendWatcher:
    def run(self):
        log("TrendWatcher running")
        while True:
            time.sleep(60)

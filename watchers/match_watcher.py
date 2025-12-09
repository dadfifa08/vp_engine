from utils.logger import log
import time

class MatchWatcher:
    def run(self):
        log("MatchWatcher running")
        while True:
            time.sleep(60)

from utils.logger import log
import time

class TikTokWatcher:
    def run(self):
        log("TikTokWatcher running")
        while True:
            time.sleep(60)

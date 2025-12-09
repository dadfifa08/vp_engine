import time
from utils.logger import log

class TikTokWatcher:
    def run(self):
        log("TikTokWatcher started")
        while True:
            time.sleep(300)
import time
from utils.logger import log

class RateLimiter:
    def __init__(self, interval=3):
        self.interval = interval
        self.last = 0

    def wait_if_needed(self):
        now = time.time()
        diff = now - self.last
        if diff < self.interval:
            sleep_time = self.interval - diff
            log("Rate limit sleep " + str(sleep_time))
            time.sleep(sleep_time)
        self.last = time.time()
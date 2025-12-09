import time
from logger import log_info

class RateLimiter:
    def __init__(self):
        self.last_action = 0
        self.cooldown = 3  

    def wait(self):
        now = time.time()
        if now - self.last_action < self.cooldown:
            delay = self.cooldown - (now - self.last_action)
            log_info(f"RateLimiter sleeping {delay:.2f}s")
            time.sleep(delay)
        self.last_action = time.time()

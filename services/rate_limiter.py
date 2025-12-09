import time

class RateLimiter:
    def __init__(self, cooldown=1):
        self.cooldown = cooldown

    def wait(self):
        time.sleep(self.cooldown)

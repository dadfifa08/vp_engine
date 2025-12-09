import time

class RateLimiter:
    def __init__(self, max_errors=5, cooldown=60):
        self.max_errors = max_errors
        self.cooldown = cooldown
        self.error_count = 0
        self.block_until = 0

    def allow(self):
        now = time.time()
        if now < self.block_until:
            return False
        return True

    def register_error(self):
        self.error_count += 1
        if self.error_count >= self.max_errors:
            self.block_until = time.time() + self.cooldown
            self.error_count = 0

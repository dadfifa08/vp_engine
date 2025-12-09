import threading
from logger import log_info

class Threader:
    def run_async(self, func):
        t = threading.Thread(target=func)
        t.start()
        log_info("Thread started.")

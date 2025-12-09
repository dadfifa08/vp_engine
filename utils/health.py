import threading, time, psutil
from utils.logger import setup_logger

logger = setup_logger("health")

def start_health_monitor():
    t = threading.Thread(target=_loop, daemon=True)
    t.start()

def _loop():
    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        if cpu > 90 or mem > 90:
            logger.warning(f"High load detected CPU={cpu}% MEM={mem}%")
        time.sleep(30)

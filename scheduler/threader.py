import time
import threading
from utils.logger import setup_logger
from scheduler.cron import run_cron_cycle

logger = setup_logger("threader")

def start_threaded_scheduler(interval_seconds: int = 60):
    """
    Runs scheduled tasks every <interval_seconds> in an isolated thread.
    """
    logger.info(f"Threaded scheduler started. Interval: {interval_seconds}s")

    def loop():
        while True:
            try:
                run_cron_cycle()
            except Exception as e:
                logger.error(f"Error in scheduler loop: {e}")

            time.sleep(interval_seconds)

    t = threading.Thread(target=loop, daemon=True)
    t.start()
    logger.info("Scheduler thread launched.")

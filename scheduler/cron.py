import time
from utils.logger import setup_logger
from scheduler.task_engine import TaskEngine
from watchers.trend_watcher import TrendWatcher

logger = setup_logger(\"cron\")

def start_scheduler():
    logger.info(\"🚀 Scheduler started\")

    engine = TaskEngine()
    engine.start(num_workers=4)

    trend = TrendWatcher()

    while True:
        try:
            engine.add_task(trend.check_trends)
        except Exception as e:
            logger.error(f\"Failed scheduling trend task → {e}\")

        time.sleep(120)  # every 2 minutes

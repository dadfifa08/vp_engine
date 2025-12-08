import threading
import queue
from utils.logger import setup_logger

logger = setup_logger(\"task_engine\")

class TaskEngine:
    def __init__(self):
        self.tasks = queue.Queue()
        self.running = True

    def add_task(self, func, *args, **kwargs):
        self.tasks.put((func, args, kwargs))

    def worker_loop(self):
        while self.running:
            try:
                func, args, kwargs = self.tasks.get()
                func(*args, **kwargs)
                self.tasks.task_done()
            except Exception as e:
                logger.error(f\"Task execution error: {e}\")

    def start(self, num_workers=3):
        for _ in range(num_workers):
            t = threading.Thread(target=self.worker_loop, daemon=True)
            t.start()
            logger.info(\"Started scheduler worker thread\")

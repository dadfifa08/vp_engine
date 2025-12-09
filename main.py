import time
import threading
from utils.logger import log

def start_scheduler():
    try:
        from scheduler.cron import run_schedule_loop
        log("Starting scheduler")
        run_schedule_loop()
    except Exception as exc:
        log(f"Scheduler failed: {exc}")

def start_autopilot():
    try:
        from autopilot.engine import start_autopilot_loop
        log("Starting autopilot")
        start_autopilot_loop()
    except Exception as exc:
        log(f"Autopilot failed: {exc}")

def start_watchers():
    try:
        from watchers.trend_watcher import TrendWatcher
        from watchers.match_watcher import MatchWatcher
        from watchers.tiktok_watcher import TikTokWatcher

        log("Starting watchers")

        watchers = [
            TrendWatcher(),
            MatchWatcher(),
            TikTokWatcher()
        ]

        for watcher in watchers:
            t = threading.Thread(target=watcher.run, daemon=True)
            t.start()
            log(f"Watcher started: {watcher.__class__.__name__}")

    except Exception as exc:
        log(f"Watcher system failed: {exc}")

def main():
    log("VP Engine booting up")

    threading.Thread(target=start_scheduler, daemon=True).start()
    threading.Thread(target=start_autopilot, daemon=True).start()
    threading.Thread(target=start_watchers, daemon=True).start()

    log("All subsystems launched")

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()

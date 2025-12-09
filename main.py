import threading
import time
from utils.logger import log

def start_scheduler():
    from scheduler.cron import run_schedule_loop
    log("Scheduler starting")
    run_schedule_loop()

def start_watchers():
    from watchers.trend_watcher import TrendWatcher
    from watchers.match_watcher import MatchWatcher
    from watchers.tiktok_watcher import TikTokWatcher

    watchers = [
        TrendWatcher(),
        MatchWatcher(),
        TikTokWatcher()
    ]

    for watcher in watchers:
        t = threading.Thread(target=watcher.run, daemon=True)
        t.start()
        log(f"Watcher started: {watcher.__class__.__name__}")

def main():
    log("VP Engine booting clean baseline")

    threading.Thread(target=start_scheduler, daemon=True).start()
    threading.Thread(target=start_watchers, daemon=True).start()

    log("All systems launched")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()

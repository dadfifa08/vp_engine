"""
MAIN ENTRYPOINT — TiraPalos Engine
----------------------------------
Boots:
• WC48 Daily Scheduler
• Tóxico Mention Auto-Replies
• TrendWatcher
• MatchWatcher
• TikTokWatcher
• Rumor engine (optional toggle)

All threads run in daemon mode for Railway compatibility.
"""

import threading
from utils.logger import log

# Scheduler (world cup autoposter)
from scheduler.cron import start_daily_worldcup_scheduler

# Watchers
from watchers.mention_watcher import MentionWatcher
from watchers.trend_watcher import TrendWatcher
from watchers.match_watcher import MatchWatcher
from watchers.tiktok_watcher import TikTokWatcher


def main():
    log("🚀 Launching TiraPalos Production Engine...")

    threads = []

    # -------------------------------------
    # WC48 daily autoposter
    # -------------------------------------
    wc_thread = threading.Thread(
        target=start_daily_worldcup_scheduler,
        name="WC48Scheduler",
        daemon=True
    )
    threads.append(wc_thread)

    # -------------------------------------
    # Toxic mention replies
    # -------------------------------------
    mentioner = MentionWatcher()
    mention_thread = threading.Thread(
        target=mentioner.run,
        name="MentionWatcher",
        daemon=True
    )
    threads.append(mention_thread)

    # -------------------------------------
    # TrendWatcher
    # -------------------------------------
    trend = TrendWatcher()
    trend_thread = threading.Thread(
        target=trend.run,
        name="TrendWatcher",
        daemon=True
    )
    threads.append(trend_thread)

    # -------------------------------------
    # MatchWatcher
    # -------------------------------------
    mw = MatchWatcher()
    match_thread = threading.Thread(
        target=mw.run,
        name="MatchWatcher",
        daemon=True
    )
    threads.append(match_thread)

    # -------------------------------------
    # TikTok Watcher
    # -------------------------------------
    tt = TikTokWatcher()
    tiktok_thread = threading.Thread(
        target=tt.run,
        name="TikTokWatcher",
        daemon=True
    )
    threads.append(tiktok_thread)

    # -------------------------------------
    # START ALL THREADS
    # -------------------------------------
    for t in threads:
        log(f"🧵 Starting thread: {t.name}")
        t.start()

    # -------------------------------------
    # KEEP PROCESS ALIVE (Railway compatible)
    # -------------------------------------
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()

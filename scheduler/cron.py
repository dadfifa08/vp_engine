import time
import schedule
from utils.logger import log
from autopilot.worldcup_poster import WorldCupPoster

poster = WorldCupPoster()

def run_cycle():
    poster.run_daily_cycle()

def start_daily_worldcup_scheduler():
    log("World Cup Scheduler started")

    # 9 AM CT = 15:00 UTC
    schedule.every().day.at("15:00").do(run_cycle)

    while True:
        schedule.run_pending()
        time.sleep(5)
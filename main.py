# main.py - Clean UTF-8 Safe Version

import time
from logger import log_info, log_error

from brain.ai_brain import AIBrain
from watchers.trend_watcher import TrendWatcher
from watchers.match_watcher import MatchWatcher
from watchers.tiktok_watcher import TikTokWatcher
from persona.persona_responder import PersonaResponder
from scheduler.threader import Threader

def start_engine():
    try:
        log_info("Starting VP Engine (Toxico Mode)")

        brain = AIBrain()
        persona = PersonaResponder()
        trends = TrendWatcher()
        matches = MatchWatcher()
        tik = TikTokWatcher()

        threader = Threader()

        def loop():
            while True:
                try:
                    t = trends.scan()
                    m = matches.watch()
                    tk = tik.detect()

                    # No posting yet — safe mode
                    log_info("Heartbeat OK.")
                    time.sleep(60)

                except Exception as inner:
                    log_error(f"Engine loop error: {str(inner)}")
                    time.sleep(10)

        threader.run_async(loop)

    except Exception as outer:
        log_error(f"Fatal error: {str(outer)}")

if __name__ == "__main__":
    start_engine()

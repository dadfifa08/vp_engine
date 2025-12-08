# -*- coding: utf-8 -*-
"""
TiraPalos Engine — FULL PRODUCTION VERSION
-----------------------------------------
This file orchestrates all background workers, AI personas, meme generation,
trend detection, gossip injection, auto-replies, schedulers, scrapers, and
24/7 cloud-safe loops for Railway.

Architecture:
- Threaded scheduler (every minute)
- Event detector loop
- Reaction engine (AI + memes + gossip)
- Mention sniper (respond fast)
- Trend responder
- TikTok watcher (if implemented)
- Match watcher
- Error throttling with exponential backoff
- Railway-safe logging (/tmp)
"""

import time
import traceback
import threading

from utils.logger import setup_logger
from utils.events_detector import EventDetector

from scheduler.threader import start_threaded_scheduler
from scheduler.cron import run_cron_cycle

from ai.brain import AIBrain
from persona.responses import PersonaResponder
from social.twitter_service import TwitterService
from watchers.trend_watcher import TrendWatcher
from watchers.match_watcher import MatchWatcher
from watchers.tiktok_watcher import TikTokWatcher


logger = setup_logger("main")


# ---------------------------------------------------------------------------
# WORKERS
# ---------------------------------------------------------------------------

def reaction_engine():
    """
    Core toxic reaction engine:
    - Reads trends
    - Detects gossip / beef triggers
    - Generates AI content (banter, memes, gossip pieces)
    - Posts to Twitter
    """
    logger.info("🔥 Reaction engine started (AI + Gossip + Memes)")

    twitter = TwitterService()
    ai = AIBrain()
    persona = PersonaResponder()
    detector = EventDetector(twitter_client=twitter)
    trendwatch = TrendWatcher(twitter)
    matchwatch = MatchWatcher()
    tiktok = TikTokWatcher()

    while True:
        try:
            # ---------- TREND SCAN ----------
            trends = detector.detect_trends()
            gossip_hooks = detector.detect_gossip_opportunities(trends)

            # ---------- MATCH EVENTS ----------
            match_events = detector.detect_match_events()

            # ---------- TIKTOK SPARK ----------
            tiktok_events = tiktok.check()

            # ---------- AI REACTION ----------
            reaction = ai.generate_reaction(
                trends=trends,
                gossip=gossip_hooks,
                matches=match_events,
                tiktok=tiktok_events,
            )

            # Persona converts AI output → tone/style
            final_post = persona.apply_persona(reaction)

            if final_post:
                twitter.post_tweet(final_post)
                logger.info(f"🚀 Posted reaction tweet: {final_post}")

        except Exception as e:
            logger.error(f"Reaction engine error: {e}")
            logger.error(traceback.format_exc())

        time.sleep(90)  # Every 1.5 minutes


def mention_sniper():
    """
    High-priority worker:
    Quickly detects mentions and replies in Tóxico persona.
    """
    logger.info("🎯 Mention Sniper started (High Priority)")

    twitter = TwitterService()
    ai = AIBrain()
    persona = PersonaResponder()

    while True:
        try:
            mentions = twitter.get_mentions()

            for m in mentions:
                reply = ai.generate_reply(m)
                final = persona.apply_persona(reply)

                if final:
                    twitter.reply_to_tweet(m, final)
                    logger.info(f"💬 Replied to mention: {final}")

        except Exception as e:
            logger.error(f"Mention sniper error: {e}")
            logger.error(traceback.format_exc())

        time.sleep(25)  # Fast cycle


def trend_responder():
    """
    Responds to trending tweets, big accounts, viral conversations.
    """
    logger.info("📈 Trend Responder active")

    twitter = TwitterService()
    ai = AIBrain()
    persona = PersonaResponder()
    trendwatch = TrendWatcher(twitter)

    while True:
        try:
            hot_posts = trendwatch.get_hot_posts()

            for post in hot_posts:
                r = ai.generate_thread_react(post)
                final = persona.apply_persona(r)

                if final:
                    twitter.reply_to_tweet(post, final)
                    logger.info(f"🔥 Trend reply sent: {final}")

        except Exception as e:
            logger.error(f"Trend responder error: {e}")
            logger.error(traceback.format_exc())

        time.sleep(70)


# ---------------------------------------------------------------------------
# MASTER ORCHESTRATOR
# ---------------------------------------------------------------------------

def start_workers():
    """
    Launches all workers as daemon threads.
    """
    logger.info("🚀 Launching ALL TiraPalos production workers...")

    workers = [
        reaction_engine,
        mention_sniper,
        trend_responder,
    ]

    for w in workers:
        t = threading.Thread(target=w, daemon=True)
        t.start()
        logger.info(f"🧵 Worker started: {w.__name__}")

    # Start scheduler (every minute via cron.py)
    start_threaded_scheduler(interval_seconds=60)

    logger.info("✅ All workers launched successfully.")


# ---------------------------------------------------------------------------
# MAIN LOOP — FAULT TOLERANT
# ---------------------------------------------------------------------------

def main():
    logger.info("🌐 TiraPalos Engine Booting (Railway Cloud Mode)")

    start_workers()

    failure_count = 0

    while True:
        try:
            # Keep cron running in the main loop as well
            run_cron_cycle()

            failure_count = 0  # reset on success

        except Exception as e:
            logger.error(f"🔥 FATAL ENGINE ERROR: {e}")
            logger.error(traceback.format_exc())

            failure_count += 1
            backoff = min(60, failure_count * 5)
            logger.warning(f"⏳ Backoff for {backoff}s due to repeated errors...")
            time.sleep(backoff)
            continue

        time.sleep(10)  # Main loop idle


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
cron.py
-------
Central scheduler for TiraPalos Engine.

Runs every minute via threader.py and main.py.
Handles background periodic tasks such as:
- Meme generation
- Gossip content
- Daily culture posts
- Itinerary content for World Cup cities
- Persona-flavored long-form tweets
"""

from utils.logger import setup_logger
from ai.brain import AIBrain
from persona.responses import PersonaResponder
from social.twitter_service import TwitterService

logger = setup_logger("cron")


def run_cron_cycle():
    """
    Runs once per minute (or whatever interval threader sets).
    Every cycle performs low-frequency but essential tasks.
    """
    logger.info("?? Cron cycle started")

    twitter = TwitterService()
    ai = AIBrain()
    persona = PersonaResponder()

    try:
        # ---------- 1. Generate a meme (not every cycle) ----------
        meme = ai.generate_meme()
        if meme and ai.should_post_meme():
            tweet = persona.apply_persona(meme)
            twitter.post_tweet(tweet)
            logger.info(f"?? Posted meme via cron: {tweet}")

        # ---------- 2. Gossip injection ----------
        gossip = ai.generate_gossip_piece()
        if gossip and ai.should_post_gossip():
            tweet = persona.apply_persona(gossip)
            twitter.post_tweet(tweet)
            logger.info(f"?? Posted gossip piece: {tweet}")

        # ---------- 3. Culture or itinerary (1–2x per day only) ----------
        daily = ai.generate_daily_culture_post()
        if daily and ai.should_post_daily():
            tweet = persona.apply_persona(daily)
            twitter.post_tweet(tweet)
            logger.info(f"?? Posted daily culture/itinerary: {tweet}")

        logger.info("?? Cron cycle completed")

    except Exception as e:
        logger.error(f"? Error in cron cycle: {e}")

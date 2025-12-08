# twitter_service.py — Production-ready Twitter posting service

import os
import logging
from social.twitter_client import TwitterClient

logger = logging.getLogger("twitter_service")
logging.basicConfig(level=logging.INFO)

class TwitterService:
    def __init__(self):
        self.client = TwitterClient()

    def post_tweet(self, text: str):
        if not text or not text.strip():
            logger.warning("Attempted to send empty tweet.")
            return False

        try:
            response = self.client.post_tweet(text)
            logger.info(f"Tweet sent successfully: {text}")
            return response

        except Exception as e:
            logger.error(f"Failed to send tweet → {e}")
            return False

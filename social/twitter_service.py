# -*- coding: utf-8 -*-
"""
twitter_service.py
------------------
Stable Twitter API wrapper for TiraPalos Engine.

Handles:
- Posting tweets
- Replying
- Fetching mentions
- Trending topics
- Rate-limit safety
- Auto-hashtag enforcement (#TiraPalos only)
"""

import time
from utils.logger import setup_logger
from twitter_api import TwitterAPI    # Make sure this is your v2 wrapper

logger = setup_logger("twitter")


class TwitterService:
    def __init__(self):
        try:
            self.client = TwitterAPI()
        except Exception as e:
            logger.error(f"❌ Failed to initialize Twitter API: {e}")
            self.client = None

    # ---------------------------------------------------------
    # Utility: enforce #TiraPalos rule
    # ---------------------------------------------------------
    def enforce_hashtag(self, text: str) -> str:
        text = text.strip()

        # Remove all hashtags except #TiraPalos
        parts = [w for w in text.split() if not w.startswith("#")]
        cleaned = " ".join(parts).strip()

        # Append allowed hashtag
        if not cleaned.endswith("#TiraPalos"):
            cleaned += " #TiraPalos"

        return cleaned

    # ---------------------------------------------------------
    # POST TWEET
    # ---------------------------------------------------------
    def post_tweet(self, text: str):
        if not text or not self.client:
            return

        text = self.enforce_hashtag(text)

        for attempt in range(3):
            try:
                self.client.tweet(text)
                logger.info(f"🐦 Tweet posted: {text}")
                return True

            except Exception as e:
                logger.error(f"Tweet post failed (attempt {attempt+1}): {e}")
                time.sleep(2 + attempt)

        logger.error("❌ Tweet post failed permanently.")
        return False

    # ---------------------------------------------------------
    # REPLY
    # ---------------------------------------------------------
    def reply_to_tweet(self, tweet_obj, text: str):
        if not text or not tweet_obj:
            return

        text = self.enforce_hashtag(text)

        for attempt in range(3):
            try:
                self.client.reply(
                    text,
                    tweet_id=tweet_obj["id"],
                    username=tweet_obj["author"]
                )
                logger.info(f"💬 Replied to {tweet_obj['id']}: {text}")
                return True

            except Exception as e:
                logger.error(f"Reply failed (attempt {attempt+1}): {e}")
                time.sleep(2 + attempt)

        logger.error("❌ Reply failed permanently.")
        return False

    # ---------------------------------------------------------
    # MENTIONS
    # ---------------------------------------------------------
    def get_mentions(self):
        try:
            mentions = self.client.get_mentions(limit=20)
            logger.info(f"📥 Mentions pulled: {len(mentions)}")
            return mentions
        except Exception as e:
            logger.error(f"Error getting mentions: {e}")
            return []

    # ---------------------------------------------------------
    # TRENDS
    # ---------------------------------------------------------
    def get_trending_topics(self):
        try:
            trends = self.client.get_trends(limit=10)
            logger.info(f"🔥 Trends pulled: {len(trends)}")
            return trends
        except Exception as e:
            logger.error(f"Error getting trends: {e}")
            return []

    # ---------------------------------------------------------
    # FETCH HOT POSTS (TREND RESPONDER)
    # ---------------------------------------------------------
    def get_hot_posts(self):
        try:
            posts = self.client.get_hot_posts(limit=10)
            logger.info(f"📊 Hot posts pulled: {len(posts)}")
            return posts
        except Exception as e:
            logger.error(f"Error getting hot posts: {e}")
            return []

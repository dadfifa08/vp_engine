# twitter_api.py
# Production-grade Twitter/X wrapper using Tweepy API v2

import os
import tweepy
from logger import log


class TwitterAPI:
    def __init__(self):
        self.api_key = os.getenv("TWITTER_API_KEY")
        self.api_secret = os.getenv("TWITTER_API_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_secret = os.getenv("TWITTER_ACCESS_SECRET")
        self.bearer = os.getenv("TWITTER_BEARER_TOKEN")

        try:
            self.client = tweepy.Client(
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_secret,
                bearer_token=self.bearer,
                wait_on_rate_limit=True
            )
            log("TwitterAPI initialized successfully")

        except Exception as e:
            log("TwitterAPI initialization error", e)
            raise

    # ---------------------------
    # Posting
    # ---------------------------
    def post_tweet(self, text):
        try:
            response = self.client.create_tweet(text=text)
            return response
        except Exception as e:
            log("Error posting tweet", e)
            return None

    # ---------------------------
    # Replying
    # ---------------------------
    def reply(self, text, tweet_id):
        try:
            response = self.client.create_tweet(
                text=text,
                in_reply_to_tweet_id=tweet_id
            )
            return response
        except Exception as e:
            log("Error replying to tweet", e)
            return None

    # ---------------------------
    # Searching recent tweets
    # ---------------------------
    def search_recent(self, query, max_results=10):
        try:
            response = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["author_id", "created_at"]
            )
            return response.data or []
        except Exception as e:
            log("Error searching tweets", e)
            return []

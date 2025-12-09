# -*- coding: utf-8 -*-
"""
TrendWatcher — Production Grade
Detects Twitter trends AND trending posts via hybrid strategy:
- Top daily Twitter trends
- Viral posts via hashtag & keyword scan
"""

from utils.logger import setup_logger
from social.twitter_service import TwitterService

logger = setup_logger("trendwatch")


class TrendWatcher:
    def __init__(self, twitter: TwitterService):
        self.twitter = twitter

    # ----------------------------------------------------------------------
    def get_trends(self):
        try:
            trends = self.twitter.get_trending_topics()
            logger.info(f"TrendWatcher: {len(trends)} trends detected.")
            return trends
        except Exception as e:
            logger.error(f"TrendWatcher trend error: {e}")
            return []

    # ----------------------------------------------------------------------
    def get_hot_posts(self):
        """
        Pulls trending tweets across multiple keywords.
        You can expand this to scrape more categories.
        """
        hot_posts = []

        keywords = [
            "world cup",
            "mexico",
            "usa",
            "argentina",
            "neymar",
            "mbappe",
            "vinicius",
            "gol",
            "penalty",
            "VAR",
        ]

        try:
            for k in keywords:
                posts = self.twitter.client.search_tweets(query=k, limit=5)
                if posts:
                    hot_posts.extend(posts)

            logger.info(f"TrendWatcher: {len(hot_posts)} hot posts found.")
            return hot_posts

        except Exception as e:
            logger.error(f"TrendWatcher hot post error: {e}")
            return []

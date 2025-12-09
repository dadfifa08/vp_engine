"""
Event Detector: analyzes social media trends, match updates, news spikes,
and determines when the AI should react with memes, gossip, tóxico banter, etc.
"""

from utils.logger import setup_logger

logger = setup_logger("events")

class EventDetector:
    def __init__(self, twitter_client=None):
        self.twitter = twitter_client

    def detect_trends(self):
        """
        Pull trending Twitter topics.
        """
        try:
            trends = self.twitter.get_trending_topics()
            logger.info(f"Detected {len(trends)} trending topics.")
            return trends
        except Exception as e:
            logger.error(f"Trend detection error: {e}")
            return []

    def detect_mentions(self):
        """
        Detect fresh mentions for auto-replies.
        """
        try:
            mentions = self.twitter.get_mentions()
            logger.info(f"Detected {len(mentions)} mentions.")
            return mentions
        except Exception as e:
            logger.error(f"Mention detection error: {e}")
            return []

    def detect_match_events(self):
        """
        Placeholder — later reads match APIs or scrapes live sources.
        """
        try:
            # TODO: Add real match watcher service
            return []
        except Exception as e:
            logger.error(f"Match event detection error: {e}")
            return []

    def detect_gossip_opportunities(self, trends):
        """
        Look for drama, beef, scandals, celebrity crossover gossip.
        """
        opportunities = []

        for t in trends:
            t_lower = t.lower()
            if any(keyword in t_lower for keyword in ["divorce", "fight", "cheating", "transfer", "scandal"]):
                opportunities.append(t)

        if opportunities:
            logger.info(f"Gossip opportunities found: {opportunities}")

        return opportunities

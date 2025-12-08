# poster.py — High-level orchestrator for posting content

from social.twitter_service import TwitterService

class Poster:
    def __init__(self):
        self.twitter = TwitterService()

    def post(self, message: str):
        return self.twitter.post_tweet(message)

# auto_reply.py — Handles auto-replies safely

from social.twitter_service import TwitterService

class AutoReply:
    def __init__(self):
        self.service = TwitterService()

    def reply(self, text: str):
        return self.service.post_tweet(text)

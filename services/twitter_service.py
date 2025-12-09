from logger import log_info, log_error
import tweepy
import os

class TwitterService:
    def __init__(self):
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        self.client = tweepy.API(auth)

    def tweet(self, text):
        try:
            self.client.update_status(text)
            log_info(f"Tweet posted: {text}")
        except Exception as e:
            log_error(f"Tweet error: {str(e)}")

import tweepy
from config import Config
from utils.logger import log

def get_client():
    auth = tweepy.OAuth1UserHandler(
        Config.API_KEY,
        Config.API_SECRET,
        Config.ACCESS_TOKEN,
        Config.ACCESS_SECRET
    )
    return tweepy.API(auth)

def post_tweet(text):
    try:
        api = get_client()
        api.update_status(text)
        log(f\"Tweet sent: {text}\")
    except Exception as e:
        log(f\"Error posting tweet: {e}\")

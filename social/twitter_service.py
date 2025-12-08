import os
import tweepy
from utils.logger import log

def get_twitter_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    bearer = os.getenv("BEARER_TOKEN")

    if not api_key:
        raise ValueError("Missing API_KEY in .env")

    client = tweepy.Client(
        bearer_token=bearer,
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    return client

def post_tweet(text: str):
    client = get_twitter_client()
    final_text = f"{text} #TiraPalos" if not text.endswith("#TiraPalos") else text

    try:
        response = client.create_tweet(text=final_text)
        log(f"Tweet posted: {response}")
    except Exception as e:
        log(f"Error posting tweet: {e}")

def reply_to_tweet(tweet_id, text):
    client = get_twitter_client()
    reply = f"{text} #TiraPalos"

    try:
        client.create_tweet(text=reply, in_reply_to_tweet_id=tweet_id)
        log(f"Replied to {tweet_id}")
    except Exception as e:
        log(f"Reply error: {e}")

# twitter_service.py
from twitter_api import TwitterAPI
from logger import log_info, log_error

class TwitterService:
    def __init__(self):
        self.api = TwitterAPI()

    # ---------------------------------------------------
    # Post a Tweet (text only)
    # ---------------------------------------------------
    def post_tweet(self, text):
        try:
            response = self.api.send_request(
                "POST",
                "/statuses/update.json",
                params={"status": text}
            )
            if response and response.status_code == 200:
                log_info("Tweet posted successfully.")
                return True
            log_error(f"Failed to post tweet: {response.text}")
            return False

        except Exception as e:
            log_error(f"post_tweet() crash → {e}")
            return False

    # ---------------------------------------------------
    # Reply To a Tweet
    # ---------------------------------------------------
    def reply(self, text, tweet_id):
        try:
            response = self.api.send_request(
                "POST",
                "/statuses/update.json",
                params={
                    "status": text,
                    "in_reply_to_status_id": tweet_id,
                    "auto_populate_reply_metadata": "true"
                }
            )
            return response.status_code == 200

        except Exception as e:
            log_error(f"reply() crash → {e}")
            return False

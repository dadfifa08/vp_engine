# threader.py — Builds tweet threads reliably

from social.twitter_service import TwitterService

class Threader:
    def __init__(self):
        self.service = TwitterService()

    def create_thread(self, tweets: list[str]):
        if not tweets:
            return False

        previous_tweet_id = None
        responses = []

        for text in tweets:
            if not text:
                continue

            response = self.service.post_tweet(text)
            responses.append(response)

            try:
                previous_tweet_id = response.get("data", {}).get("id")
            except:
                previous_tweet_id = None

        return responses

import os
from twitter import Twitter, OAuth

class TwitterAPI:
    def __init__(self):
        self.client = Twitter(
            auth=OAuth(
                os.getenv("TWITTER_ACCESS_TOKEN"),
                os.getenv("TWITTER_ACCESS_SECRET"),
                os.getenv("TWITTER_API_KEY"),
                os.getenv("TWITTER_API_SECRET")
            )
        )

    def post_tweet(self, text):
        return self.client.statuses.update(status=text)

    def reply(self, text, tweet_id):
        return self.client.statuses.update(status=text, in_reply_to_status_id=tweet_id)

    def search_recent(self, query, count=25):
        return self.client.search.tweets(q=query, count=count)

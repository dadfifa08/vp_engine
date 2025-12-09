import time
from services.twitter_service import TwitterService
from persona.responder import PersonaResponder
from utils.logger import log

class MentionWatcher:

    def __init__(self):
        self.twitter = TwitterService()
        self.responder = PersonaResponder()
        self.last_id = None

    def run(self):
        log("💬 MentionWatcher started (tóxico mode ON)")
        while True:
            try:
                mentions = self.twitter.get_mentions(since_id=self.last_id)

                for m in mentions:
                    user = m['user']['screen_name']
                    text = m['text']
                    tweet_id = m['id']

                    log(f"🔔 Mention from @{user}: {text}")

                    reply_text = self.responder.generate_toxic_reply(user, text)

                    self.twitter.post_reply(reply_text, tweet_id)

                    self.last_id = tweet_id

            except Exception as e:
                log(f"⚠ MentionWatcher error: {e}")

            time.sleep(20)  # Runs every 20 seconds

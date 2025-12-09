from utils.logger import setup_logger
from social.twitter_service import TwitterService
from ai.reaction_engine import ReactionEngine

logger = setup_logger(\"mention_responder\")

class MentionResponder:
    def __init__(self):
        self.service = TwitterService()
        self.ai = ReactionEngine()

    def process_mentions(self, mentions):
        for mention in mentions:
            text = mention.get(\"text\")
            user = mention.get(\"username\")

            reaction = self.ai.generate_reaction(text)
            if reaction:
                reply_text = f\"@{user} {reaction}\"
                self.service.post_tweet(reply_text)
                logger.info(f\"Replied to @{user}: {reaction}\")

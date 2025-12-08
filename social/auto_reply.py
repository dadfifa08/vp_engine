import tweepy
from persona.persona import ToxicoPersona

bot = ToxicoPersona()

class AutoReply:
    def __init__(self, api):
        self.api = api

    def reply_to_tweet(self, tweet):
        mensaje = bot.generate_comment()
        self.api.update_status(
            status=f"@{tweet.user.screen_name} {mensaje}",
            in_reply_to_status_id=tweet.id
        )

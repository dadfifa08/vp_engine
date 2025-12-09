import time
from utils.logger import log
from persona.responder import PersonaResponder
from services.twitter_service import TwitterService

class MatchWatcher:
    def __init__(self):
        self.twitter = TwitterService()
        self.persona = PersonaResponder()

    def run(self):
        log("MatchWatcher started")
        while True:
            time.sleep(60)

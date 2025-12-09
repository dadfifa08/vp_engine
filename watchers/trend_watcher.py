import time
from utils.logger import log
from persona.responder import PersonaResponder
from services.twitter_service import TwitterService

class TrendWatcher:
    def __init__(self):
        self.twitter = TwitterService()
        self.persona = PersonaResponder()

    def run(self):
        log("TrendWatcher started")
        while True:
            # Placeholder until real trend API is integrated
            time.sleep(300)
import random
from persona.toxicity import ToxicoPersona
from persona.gossip import GossipPersona
from persona.banter import BanterPersona
from ai.sentiment import SentimentAnalyzer

class DynamicPersonaRouter:
    def __init__(self):
        self.sentiment = SentimentAnalyzer()
        self.toxico = ToxicoPersona()
        self.gossip = GossipPersona()
        self.banter = BanterPersona()

    def pick(self, text: str):
        mood = self.sentiment.classify(text)

        if mood == \"negative\":
            return self.toxico
        elif mood == \"neutral\":
            return self.banter
        else:
            return self.gossip

import random
from persona.toxicity import ToxicoPersona
from persona.gossip import GossipPersona
from persona.banter import BanterPersona

class PersonaRouter:
    PERSONAS = [
        ToxicoPersona(),
        GossipPersona(),
        BanterPersona()
    ]

    def pick_persona(self):
        return random.choice(self.PERSONAS)

# -*- coding: utf-8 -*-
"""
PersonaResponder — Production Grade
Applies the proper tone:
- Tóxico (default)
- Informative
- Gossip (super tóxico)
- Banter (playful)
"""

from utils.logger import setup_logger

logger = setup_logger("persona")


class PersonaResponder:
    def __init__(self):
        pass

    # ----------------------------------------
    def apply_persona(self, text: str, mode="auto"):
        if not text:
            return None

        # Gossip overrides everything
        if "gossip" in text.lower() or "chisme" in text.lower():
            mode = "gossip"

        if mode == "auto":
            if "World Cup" in text or "culture" in text:
                mode = "informative"
            else:
                mode = "toxico"

        if mode == "toxico":
            return self.toxico(text)

        if mode == "informative":
            return self.informative(text)

        if mode == "gossip":
            return self.gossip(text)

        if mode == "banter":
            return self.banter(text)

        return text

    # ----------------------------------------
    def toxico(self, text):
        return f"{text.strip()} 😭🔥🤡 #TiraPalos"

    def informative(self, text):
        return f"{text.strip()} #TiraPalos"

    def gossip(self, text):
        return f"CHISME BOMBA 💣🔥: {text.strip()} #TiraPalos"

    def banter(self, text):
        return f"{text.strip()} 😂⚽️ #TiraPalos"

from utils.logger import log

class PersonaResponder:
    def reply(self, text):
        log(f"Persona responder received: {text}")
        return text

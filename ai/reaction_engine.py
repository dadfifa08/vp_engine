from utils.logger import setup_logger
from utils.rate_limiter import RateLimiter
from persona.persona_router import PersonaRouter
import random

logger = setup_logger(\"reaction_engine\")

class ReactionEngine:
    def __init__(self):
        self.limiter = RateLimiter(max_errors=10, cooldown=60)
        self.router = PersonaRouter()

    def scrape_headlines(self):
        return [
            \"Messi rumored to skip training!\",
            \"World Cup hotels nearly sold out!\",
            \"Mexico fans causing chaos already!\"
        ]

    def generate_reaction(self, headline: str) -> str:
        if not self.limiter.allow():
            logger.warning(\"Rate-limiter active. Skipping reaction generation.\")
            return None

        persona = self.router.pick_persona()
        reaction = persona.generate(headline)

        logger.info(f\"Generated reaction → {reaction}\")
        return reaction

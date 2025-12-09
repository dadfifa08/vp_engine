import os
import random
from openai import OpenAI
from logger import log


class AIBrain:
    """
    Central intelligence engine for:
    - Toxic banter mode
    - Rumor generation
    - Celebrity × football crossover gossip
    - Informational content
    - Meme caption creation
    - Replies to trending posts
    """

    def __init__(self, mode="toxico"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.mode = mode

    # ---------------------------
    # Core prompt builders
    # ---------------------------

    def _build_system_prompt(self):
        if self.mode == "toxico":
            return (
                "You are TiraPalos — an aggressive, instigating, Mexican-American football "
                "tóxico personality. You connect drama that shouldn't be connected, you gossip, "
                "you stir rivalries, you exaggerate, you drop Latino inside jokes, "
                "and you are hilarious and chaotic. No hashtags allowed except #TiraPalos at end."
            )

        if self.mode == "informative":
            return (
                "You generate accurate, clean, useful content about World Cup 2026, "
                "host cities, match previews, tactical breakdowns, travel guides."
            )

        if self.mode == "rumors":
            return (
                "Generate outrageous but semi-plausible celebrity × football crossover rumors. "
                "Example: linking divorces, breakups, cheating scandals, vacations, "
                "to football performance or transfers. Make it spicy, chaotic and creative."
            )

        return "You are a general-purpose creative writer. Produce engaging content."

    # ---------------------------
    # Main generator
    # ---------------------------

    def generate(self, context):
        """Generic text generation engine"""

        try:
            system_prompt = self._build_system_prompt()

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context},
                ],
                max_tokens=300,
                temperature=1.1 if self.mode == "toxico" else 0.9,
            )

            text = response.choices[0].message.content.strip()

            # Force brand tag
            if not text.endswith("#TiraPalos"):
                text += " #TiraPalos"

            return text

        except Exception as e:
            log("AIBrain generation error", e)
            return None

    # ---------------------------
    # Specialized modes
    # ---------------------------

    def generate_toxic_reply(self, tweet_text, author):
        prompt = (
            f"Reply tóxico to this tweet:\n\n"
            f"Tweet: {tweet_text}\nAuthor: {author}\n\n"
            f"Be savage, chaotic, funny, Latino-coded, instigating rivalries. "
        )
        return self.generate(prompt)

    def generate_meme_caption(self, topic):
        prompt = (
            f"Generate a meme caption about: {topic}\n"
            f"Funny, toxic, chaotic, Mexican-American humor."
        )
        return self.generate(prompt)

    def generate_rumor(self, person_a, person_b):
        prompt = (
            f"Generate a football × celebrity rumor involving {person_a} and {person_b}. "
            f"Be outrageous, but with a hint of plausibility. Maximum chisme."
        )
        return self.generate(prompt)

    def generate_worldcup_info(self, query):
        prompt = (
            f"Create an informative piece related to World Cup 2026 about: {query}."
        )
        return self.generate(prompt)

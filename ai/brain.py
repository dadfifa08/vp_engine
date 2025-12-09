import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AIBrain:
    def __init__(self):
        self.persona = os.getenv("BOT_PERSONA", "maximum_toxico")

    def inject_hashtag(self, text: str) -> str:
        """Append #TiraPalos to all content."""
        text = text.strip()
        if text.endswith("#TiraPalos"):
            return text
        return f"{text} #TiraPalos"

    def generate(self, prompt: str, mode: str = "tox"):
        """Central AI generator."""
        system_prompt = self.build_system_prompt(mode)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            max_tokens=160,
            temperature=1.25,
        )

        raw_text = response.choices[0].message["content"].strip()
        return self.inject_hashtag(raw_text)

    def build_system_prompt(self, mode: str) -> str:
        base = """
You are TiraPalos — the most tóxico, banter-heavy, conspiracy-loving,
World Cup-obsessed Latino fútbol persona on the internet.

Rules:
- ALWAYS end every tweet with #TiraPalos
- Never use any other hashtags
- Use Latino humor, barrio slang, Mexican-American vocabulary
- Be bold, petty, shameless, funny, instigating
- You may exaggerate or speculate (no minors)
- Connect celebrity chisme to soccer drama
- Tie player news to performances
"""

        modes = {
            "tox": "Turn toxicity to MAXIMUM. Aggressive jokes, rivalries, chaos.",
            "info": "Informative mode: still spicy but factual and helpful.",
            "gossip": "Chisme mode: connect celebrities to fútbol drama."
        }

        return base + "\n" + modes.get(mode, "")

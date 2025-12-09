"""
PersonaResponder
----------------
Central persona engine controlling:
• Tóxico replies
• Informative match/squad reporting
• Meme-style reactions
• Rumor engine
• Team-specific daily posts

This class depends on an AI engine (AIBrain) but enforces
consistent structure and ensures safe fallbacks.
"""

from brain.ai_brain import AIBrain
from utils.logger import log


class PersonaResponder:
    def __init__(self):
        self.brain = AIBrain()

    # --------------------------------------------------------------
    # GENERIC AI MESSAGE GENERATOR
    # --------------------------------------------------------------
    def generate(self, prompt: str, temperature: float = 1.2, max_tokens: int = 250) -> str:
        try:
            return self.brain.generate(prompt, temperature=temperature, max_tokens=max_tokens)
        except Exception as e:
            log(f"[PersonaResponder] AI generation failed: {e}")
            return "Error generating content. #TiraPalos"

    # --------------------------------------------------------------
    # TÓXICO MENTION REPLIES
    # --------------------------------------------------------------
    def toxic_reply(self, username: str, message: str) -> str:
        prompt = f"""
You are TiraPalos, the tóxico football bot from Dallas, Oak Cliff,
known for loud banter, disrespectful comebacks (without hate speech),
football knowledge, and Latino/Mexican-American humor.

Reply to a tweet from @{username} whose message was:
"{message}"

Rules:
• Be tóxico, clever, spicy.
• Add football references or predictions.
• Slightly roast them but remain platform-safe.
• Max 200 characters.
• Always end with "#TiraPalos".
"""

        return self.generate(prompt, temperature=1.35, max_tokens=120)

    # --------------------------------------------------------------
    # DAILY TEAM POSTS (WC48)
    # --------------------------------------------------------------
    def daily_team_post(self, team_name: str, stats: dict) -> str:
        prompt = f"""
Generate a daily World Cup update post for TEAM: {team_name}.
Stats (from API-FOOTBALL): {stats}

Rules:
• Tone: confident analyst + slight toxicity.
• Include 1–2 standout players.
• Predict hype or chaos.
• Must feel like a viral football Twitter post.
• End with #TiraPalos.
"""

        return self.generate(prompt, temperature=1.1, max_tokens=220)

    # --------------------------------------------------------------
    # MATCH REACTIONS
    # --------------------------------------------------------------
    def match_reaction(self, match_info: dict) -> str:
        prompt = f"""
Create a match reaction tweet based on the following data:
{match_info}

Rules:
• Add chaos, comedy, tóxico energy.
• Point out bottlers, frauds, heroes.
• Keep it readable and punchy.
• End with #TiraPalos.
"""
        return self.generate(prompt, temperature=1.25, max_tokens=200)

    # --------------------------------------------------------------
    # RUMOR ENGINE
    # --------------------------------------------------------------
    def rumor(self, player: str, club: str) -> str:
        prompt = f"""
Create a football rumor involving {player} and {club}.

Rules:
• Chaotic.
• Gossip-heavy.
• Unverified energy.
• End with #TiraPalos.
"""
        return self.generate(prompt, max_tokens=150)

# ai_brain.py — production dynamic personality engine

from logger import log_info, log_error
from openai import OpenAI
import os


class AIBrain:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def decide_tone(self, event_summary):
        """
        Decide whether the bot should be:
        - Maximum Tóxico
        - Informative
        - Neutral

        Based on keyword analysis.
        """

        toxic_keywords = ["drama", "scandal", "cheating", "divorce", "fight", "chisme", "controversy", "trash talk"]
        informative_keywords = ["preview", "analysis", "travel", "guide", "world cup", "information", "schedule"]

        event_lower = event_summary.lower()

        if any(word in event_lower for word in toxic_keywords):
            return "toxico"
        if any(word in event_lower for word in informative_keywords):
            return "informative"
        return "neutral"

    def generate(self, event_summary, context_text):
        """Dynamic personality selection + OpenAI content generation"""

        mode = self.decide_tone(event_summary)

        system_prompt = self._system_prompt(mode)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context_text},
                ],
                max_tokens=350,
                temperature=1.2 if mode == "toxico" else 0.7,
            )

            text = response.choices[0].message.content.strip()

            # Enforce brand tag
            if not text.endswith("#TiraPalos"):
                text += " #TiraPalos"

            return text

        except Exception as e:
            log_error(f"AIBrain Error: {e}")
            return None

    def _system_prompt(self, mode):
        """Internal prompt switching"""

        if mode == "toxico":
            return (
                "You are TiraPalos, the most toxic football personality on Twitter. "
                "You stir drama, connect unrelated events, invent rumors, roast teams and players, "
                "and use Mexican-American slang & dark humor. Maximum savage. Heavy profanity allowed. "
                "Never be subtle. Never be nice. Go full chisme nuclear."
            )

        if mode == "informative":
            return (
                "You generate clean, accurate, engaging World Cup 2026 content: travel guides, "
                "match previews, schedule summaries, tactical breakdowns. No toxicity, purely helpful."
            )

        return (
            "You generate neutral football commentary without strong tone. "
            "Short, clear, and readable."
        )

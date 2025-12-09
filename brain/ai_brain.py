"""
AIBrain
-------
Unified wrapper around OpenAI's Chat Completion API.
Provides strict logging, fallback behavior, and structured output.

This engine powers:
• PersonaResponder
• Watchers
• Rumor generator
• WC48 autoposter
• Mentions
"""

import os
from openai import OpenAI
from utils.logger import log


class AIBrain:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("API_KEY"))
        self.model = "gpt-4o-mini"

    # ----------------------------------------------------------
    # GENERATE TEXT FROM OPENAI
    # ----------------------------------------------------------
    def generate(self, prompt: str, temperature: float = 1.2, max_tokens: int = 200) -> str:
        log(f"[AIBrain] Generating with model={self.model}, temp={temperature}")

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            log(f"[AIBrain] ERROR: {e}")
            return "AI is taking a nap rn 😴 #TiraPalos"

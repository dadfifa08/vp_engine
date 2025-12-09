# -*- coding: utf-8 -*-
"""
AIBrain — Production Grade
Handles:
- Reactions
- Memes
- Gossip
- Culture posts
- Thread reactions
- Replies
Uses OpenAI GPT-4o / GPT-4o-mini
"""

import os
import openai
from utils.logger import setup_logger

logger = setup_logger("brain")

openai.api_key = os.getenv("OPENAI_API_KEY")


class AIBrain:
    def __init__(self):
        self.model = "gpt-4o-mini"

    # ------------------------------------------------------------------
    def call(self, prompt: str):
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            return response.choices[0].message["content"]
        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            return None

    # ------------------------------------------------------------------
    def generate_reaction(self, trends=[], gossip=[], matches=[], tiktok=[]):
        prompt = f"""
Eres un narrador tóxico, gracioso, y Mexa-Americano.
Responde con banter, picardía, chisme, y reacciones exageradas.
Trends: {trends}
Gossip hooks: {gossip}
Match events: {matches}
TikTok sparks: {tiktok}

Generate ONE chaotic reaction tweet (short).
Include Spanglish, slang, fútbol toxicity.
Do NOT include any hashtags except append '#TiraPalos' at the end.
"""
        return self.call(prompt)

    # ------------------------------------------------------------------
    def generate_reply(self, mention):
        prompt = f"""
User tweeted: {mention}
Respond como un compa tóxico, but funny.
Keep it short and spicy.
"""
        return self.call(prompt)

    # ------------------------------------------------------------------
    def generate_thread_react(self, post):
        prompt = f"""
React tóxicamente to this viral tweet:
{post}

Keep it petty, soccer-themed, and Mexa-Chicano spicy.
"""
        return self.call(prompt)

    # ------------------------------------------------------------------
    def generate_meme(self):
        prompt = """
Create a meme caption about fútbol, drama, or the World Cup.
Short, punchy, toxic, and viral.
"""
        return self.call(prompt)

    # ------------------------------------------------------------------
    def generate_gossip_piece(self):
        prompt = """
Invent or exaggerate un chisme futbolero.
Make it spicy but not defamatory.
Short and chaotic.
"""
        return self.call(prompt)

    # ------------------------------------------------------------------
    def generate_daily_culture_post(self):
        prompt = """
Create an informative but fun post about:
- A World Cup city
- Food
- Culture
- Traditions
Make it helpful and cool.
"""
        return self.call(prompt)

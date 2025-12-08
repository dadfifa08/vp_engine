from utils.logger import setup_logger
import random

logger = setup_logger(\"meme_gen\")

class MemeGenerator:
    MEME_TEMPLATES = [
        \"When {{team}} fans realize they’re not making playoffs 😭\",
        \"POV: You believed {{player}} would carry the squad 💀\",
    ]

    def create_meme(self, context: str) -> str:
        template = random.choice(self.MEME_TEMPLATES)
        meme = template.replace(\"{{team}}\", context).replace(\"{{player}}\", context)
        logger.info(f\"Generated meme → {meme}\")
        return meme

import random
from utils.logger import setup_logger

logger = setup_logger(\"predictor\")

class MatchPredictor:
    def predict(self, team_a: str, team_b: str):
        outcomes = [
            f\"{team_a} wins narrowly\",
            f\"{team_b} pulls an upset\",
            f\"High scoring draw expected\"
        ]
        result = random.choice(outcomes)
        logger.info(f\"Predicted: {result}\")
        return result

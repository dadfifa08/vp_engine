from textblob import TextBlob
from utils.logger import setup_logger

logger = setup_logger(\"sentiment\")

class SentimentAnalyzer:
    def classify(self, text: str):
        score = TextBlob(text).sentiment.polarity

        if score > 0.3:
            sentiment = \"positive\"
        elif score < -0.3:
            sentiment = \"negative\"
        else:
            sentiment = \"neutral\"

        logger.info(f\"Sentiment for '{text}' → {sentiment} ({score})\")
        return sentiment

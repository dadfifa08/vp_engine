import base64
import requests
from utils.logger import setup_logger

logger = setup_logger(\"image_meme\")

class ImageMemeGenerator:
    def __init__(self):
        self.api_url = \"https://api.openai.com/v1/images/generations\"
        self.api_key = os.getenv(\"OPENAI_API_KEY\")

    def generate_meme(self, text_prompt: str):
        try:
            headers = {\"Authorization\": f\"Bearer {self.api_key}\"}
            payload = {
                \"model\": \"gpt-image-1\",
                \"prompt\": text_prompt,
                \"size\": \"1024x1024\"
            }

            response = requests.post(self.api_url, json=payload, headers=headers)
            data = response.json()

            img_b64 = data[\"data\"][0][\"b64_json\"]
            logger.info(f\"Generated meme for: {text_prompt}\")

            return base64.b64decode(img_b64)

        except Exception as e:
            logger.error(f\"AI meme generator failed → {e}\")
            return None

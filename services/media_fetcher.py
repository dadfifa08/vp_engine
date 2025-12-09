import os
import requests
import random
from utils.logger import log

class MediaFetcher:
    """
    Fetches a relevant, copyright-safe image or GIF using a CC-search engine.
    Falls back to a meme generator endpoint if needed.
    """

    CC_SEARCH_URL = "https://api.duckduckgo.com/"
    SAVE_DIR = "downloads"

    def __init__(self):
        if not os.path.exists(self.SAVE_DIR):
            os.makedirs(self.SAVE_DIR)

    def fetch_image(self, query: str) -> str:
        """
        Returns a file path to a downloaded image.
        """

        log(f"🔎 Searching media for: {query}")

        params = {
            "q": query,
            "format": "json",
            "ia": "images"
        }

        try:
            resp = requests.get(self.CC_SEARCH_URL, params=params, timeout=5)
            data = resp.json()

            images = [
                item["image"]
                for item in data.get("results", [])
                if "image" in item
            ]

            if not images:
                raise ValueError("No images found")

            url = random.choice(images)
            ext = ".jpg"
            out_path = os.path.join(self.SAVE_DIR, f"media_{random.randint(1000,9999)}{ext}")

            img = requests.get(url, timeout=5)
            with open(out_path, "wb") as f:
                f.write(img.content)

            log(f"📸 Downloaded image: {out_path}")
            return out_path

        except Exception as e:
            log(f"⚠ Media search failed, fallback to meme: {e}")
            return self.generate_fallback_meme(query)

    def generate_fallback_meme(self, topic: str) -> str:
        """
        Uses a public meme generator fallback.
        """
        meme_url = "https://api.memegen.link/images/custom/-/{topic}.jpg?background=https://picsum.photos/1200"
        meme_url = meme_url.replace("{topic}", topic.replace(" ", "%20"))

        out_path = os.path.join(self.SAVE_DIR, f"meme_{random.randint(1000,9999)}.jpg")
        img = requests.get(meme_url)

        with open(out_path, "wb") as f:
            f.write(img.content)

        log(f"🎨 Meme fallback created: {out_path}")
        return out_path

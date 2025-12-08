# twitter_client.py — Handles authentication + direct Twitter API calls

import os
import logging
import requests

logger = logging.getLogger("twitter_client")

class TwitterClient:
    def __init__(self):
        self.bearer_token = os.getenv("BEARER_TOKEN")
        self.api_url = "https://api.twitter.com/2/tweets"

        if not self.bearer_token:
            raise ValueError("Missing BEARER_TOKEN environment variable")

    def post_tweet(self, text: str):
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        
        payload = {"text": text}

        response = requests.post(self.api_url, json=payload, headers=headers)

        if response.status_code not in (200, 201):
            logger.error(f"Twitter API error {response.status_code}: {response.text}")
            raise Exception(response.text)

        return response.json()

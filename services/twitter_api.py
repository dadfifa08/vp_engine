# twitter_api.py
import time
import random
import hashlib
import hmac
import base64
import urllib.parse
import requests
from logger import log_error, log_info

class TwitterAPI:
    BASE_URL = "https://api.twitter.com/1.1"

    def __init__(self):
        from config import (
            TWITTER_API_KEY,
            TWITTER_API_SECRET,
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_SECRET
        )

        self.consumer_key = TWITTER_API_KEY
        self.consumer_secret = TWITTER_API_SECRET
        self.access_token = TWITTER_ACCESS_TOKEN
        self.access_secret = TWITTER_ACCESS_SECRET

    def _generate_oauth_headers(self, method, url, params=None):
        if params is None:
            params = {}

        oauth_params = {
            "oauth_consumer_key": self.consumer_key,
            "oauth_nonce": hashlib.sha1(str(random.random()).encode()).hexdigest(),
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_timestamp": str(int(time.time())),
            "oauth_token": self.access_token,
            "oauth_version": "1.0"
        }

        all_params = {**params, **oauth_params}
        sorted_params = "&".join(
            f"{urllib.parse.quote(k, safe='')}={urllib.parse.quote(v, safe='')}"
            for k, v in sorted(all_params.items())
        )

        base_string = "&".join([
            method.upper(),
            urllib.parse.quote(url, safe=''),
            urllib.parse.quote(sorted_params, safe='')
        ])

        signing_key = f"{urllib.parse.quote(self.consumer_secret)}&{urllib.parse.quote(self.access_secret)}"

        signature = hmac.new(
            signing_key.encode(),
            base_string.encode(),
            hashlib.sha1
        ).digest()

        oauth_params["oauth_signature"] = base64.b64encode(signature).decode()

        header = "OAuth " + ", ".join(
            f'{k}="{urllib.parse.quote(v)}"' for k, v in oauth_params.items()
        )

        return {"Authorization": header}

    def send_request(self, method, endpoint, params=None, json=None):
        url = f"{self.BASE_URL}{endpoint}"

        headers = self._generate_oauth_headers(method, url, params)
        try:
            response = requests.request(method, url, headers=headers, params=params, json=json)

            if response.status_code >= 400:
                log_error(f"Twitter Error {response.status_code}: {response.text}")

            return response
        except Exception as e:
            log_error(f"Twitter Request Failed: {e}")
            return None

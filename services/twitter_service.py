import os
import time
import json
import hmac
import base64
import hashlib
import random
import string
import urllib.parse
import requests

from utils.logger import log
from utils.rate_limiter import RateLimiter


class TwitterService:
    POST_TWEET_URL = "https://api.twitter.com/2/tweets"
    POST_REPLY_URL = "https://api.twitter.com/2/tweets"
    GET_MENTIONS_URL = "https://api.twitter.com/2/users/{user_id}/mentions"
    UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"

    def __init__(self):
        self.consumer_key = os.getenv("API_KEY")
        self.consumer_secret = os.getenv("API_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        self.bearer = os.getenv("BEARER_TOKEN")
        self.rate = RateLimiter()

        if not all([self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret]):
            raise RuntimeError("Missing OAuth credentials")

    def _enc(self, s):
        return urllib.parse.quote(str(s), safe="")

    def _nonce(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

    def _timestamp(self):
        return str(int(time.time()))

    def _sign(self, method, url, params, token_secret=""):
        encoded = "&".join(f"{self._enc(k)}={self._enc(v)}" for k, v in sorted(params.items()))
        base = "&".join([method.upper(), self._enc(url), self._enc(encoded)])
        key = f"{self._enc(self.consumer_secret)}&{self._enc(token_secret)}"
        hashed = hmac.new(key.encode(), base.encode(), hashlib.sha1)
        return base64.b64encode(hashed.digest()).decode()

    def _oauth_header(self, params):
        return "OAuth " + ", ".join(f'{self._enc(k)}="{self._enc(v)}"' for k, v in params.items())

    def _request(self, method, url, payload=None):
        oauth = {
            "oauth_consumer_key": self.consumer_key,
            "oauth_nonce": self._nonce(),
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_timestamp": self._timestamp(),
            "oauth_token": self.access_token,
            "oauth_version": "1.0"
        }

        signature = self._sign(method, url, oauth, self.access_token_secret)
        oauth["oauth_signature"] = signature

        headers = {
            "Authorization": self._oauth_header(oauth),
            "Content-Type": "application/json"
        }

        if method == "POST":
            r = requests.post(url, headers=headers, json=payload)
        else:
            r = requests.get(url, headers=headers, params=payload)

        if r.status_code >= 400:
            log("Twitter error " + str(r.status_code) + " " + r.text)
            raise RuntimeError("Twitter API error")

        return r.json()

    def post_tweet(self, text, media_ids=None):
        self.rate.wait_if_needed()

        payload = {"text": text}
        if media_ids:
            payload["media"] = {"media_ids": media_ids}

        return self._request("POST", self.POST_TWEET_URL, payload)

    def post_reply(self, text, reply_to_id):
        self.rate.wait_if_needed()

        payload = {
            "text": text,
            "reply": {"in_reply_to_tweet_id": reply_to_id}
        }
        return self._request("POST", self.POST_REPLY_URL, payload)

    def get_mentions(self, since_id=None):
        user_id = os.getenv("TWITTER_USER_ID")
        url = self.GET_MENTIONS_URL.replace("{user_id}", user_id)
        params = {}
        if since_id:
            params["since_id"] = since_id

        headers = {"Authorization": f"Bearer {self.bearer}"}
        r = requests.get(url, headers=headers, params=params)

        if r.status_code >= 400:
            log("Error loading mentions: " + r.text)
            return []

        data = r.json().get("data", [])
        return data

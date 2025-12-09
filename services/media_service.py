import os
import mimetypes
import requests
from utils.logger import log


class MediaService:
    UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"

    def __init__(self, twitter):
        self.twitter = twitter

    def upload(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError("Missing media file: " + filepath)

        mime = mimetypes.guess_type(filepath)[0] or "application/octet-stream"
        size = os.path.getsize(filepath)

        init = requests.post(
            self.UPLOAD_URL,
            data={"command": "INIT", "total_bytes": size, "media_type": mime},
            auth=(self.twitter.consumer_key, self.twitter.consumer_secret)
        )

        media_id = init.json().get("media_id_string")

        with open(filepath, "rb") as f:
            segment = f.read()
            requests.post(
                self.UPLOAD_URL,
                data={"command": "APPEND", "media_id": media_id, "segment_index": 0},
                files={"media": segment},
                auth=(self.twitter.consumer_key, self.twitter.consumer_secret)
            )

        fin = requests.post(
            self.UPLOAD_URL,
            data={"command": "FINALIZE", "media_id": media_id},
            auth=(self.twitter.consumer_key, self.twitter.consumer_secret)
        )

        log("Media uploaded " + str(media_id))
        return media_id

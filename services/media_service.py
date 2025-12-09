from twitter_api import TwitterAPI
from logger import log_error, log_info

class MediaService:
    def __init__(self):
        self.api = TwitterAPI()

    def upload_image(self, image_path):
        try:
            with open(image_path, "rb") as f:
                binary = f.read()

            response = self.api.send_request(
                "POST",
                "/media/upload.json",
                params={"media": binary}
            )

            if response and response.status_code == 200:
                media_id = response.json()["media_id_string"]
                log_info(f"Media uploaded ? ID: {media_id}")
                return media_id

            log_error(f"Upload failed: {response.text}")
            return None

        except Exception as e:
            log_error(f"upload_image() crash ? {e}")
            return None

import os

class Config:
    API_KEY = os.getenv('X_API_KEY')
    API_SECRET = os.getenv('X_API_SECRET')
    ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
    ACCESS_SECRET = os.getenv('X_ACCESS_SECRET')

    # 24/7 mode settings
    POST_INTERVAL = 300   # 5 minutes
    REPLY_INTERVAL = 180  # 3 minutes

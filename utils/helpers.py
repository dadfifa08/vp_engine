import time
import random
import hashlib

def short_id(text: str) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:10]

def sleep_random(min_s: int = 2, max_s: int = 5):
    time.sleep(random.randint(min_s, max_s))

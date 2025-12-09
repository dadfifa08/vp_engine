import datetime
import sys

def _ts():
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def log_info(message):
    print(f"[INFO] {_ts()} {message}", file=sys.stdout, flush=True)

def log_error(message):
    print(f"[ERROR] {_ts()} {message}", file=sys.stderr, flush=True)

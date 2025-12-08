from scheduler.cron import start_scheduler
from health import check_health
from utils.logger import setup_logger
from flask import Flask, jsonify
import threading

logger = setup_logger(\"main\")

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(check_health())

def background_worker():
    logger.info(\"Starting scheduler engine...\")
    start_scheduler()

if __name__ == '__main__':
    threading.Thread(target=background_worker, daemon=True).start()

    logger.info(\"Flask health server running on port 8080…\")
    app.run(host='0.0.0.0', port=8080)

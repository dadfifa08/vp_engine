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

def run_scheduler():
    logger.info(\"Starting background scheduler...\")
    start_scheduler()

if __name__ == '__main__':
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

    logger.info(\"Starting Flask health server...\")
    app.run(host='0.0.0.0', port=8080)

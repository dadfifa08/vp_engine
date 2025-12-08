from flask import Flask
from utils.logger import log

app = Flask(__name__)

@app.route("/")
def home():
    return "TiraPalos Engine is Running (Maximum Tóxico Mode)"

if __name__ == "__main__":
    log("Starting Flask uptime server…")
    app.run(host="0.0.0.0", port=8080)

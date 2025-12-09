import logging
import sys

class VPEngineLogger:
    def __init__(self):
        self.logger = logging.getLogger("vp_engine")
        self.logger.setLevel(logging.INFO)
        self.logger.handlers.clear()

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        ))
        self.logger.addHandler(handler)

    def log(self, message):
        self.logger.info(message)

_logger = VPEngineLogger()

def log(message):
    _logger.log(message)

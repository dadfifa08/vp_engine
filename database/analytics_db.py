import sqlite3
from utils.logger import setup_logger

logger = setup_logger('analytics')

class AnalyticsDB:
    def __init__(self):
        self.conn = sqlite3.connect('analytics.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT,
                payload TEXT
            )
        ''')
        self.conn.commit()

    def log(self, event, payload=None):
        c = self.conn.cursor()
        c.execute('INSERT INTO events (event, payload) VALUES (?, ?)', (event, str(payload)))
        self.conn.commit()

    def fetch_all(self):
        c = self.conn.cursor()
        return c.execute('SELECT event, payload FROM events').fetchall()

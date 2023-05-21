# user.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'FirstBite.db'
FIRSTBITE_DB = sqlite3.connect(DB_FILE)
FIRSTBITE_DB.row_factory = sqlite3.Row

cur = FIRSTBITE_DB.cursor()
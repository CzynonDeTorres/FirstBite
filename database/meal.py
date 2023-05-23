# meal.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

FOOD_DB_FILE = CURRENT_DIR / 'food.db'
FOOD_DB = sqlite3.connect(FOOD_DB_FILE)
FOOD_DB.row_factory = sqlite3.Row
FOOD_cur = FOOD_DB.cursor()

USER_DB_FILE = CURRENT_DIR / 'user.db'
USER_DB = sqlite3.connect(USER_DB_FILE)
USER_DB.row_factory = sqlite3.Row
USER_cur = USER_DB.cursor()

def show_meal():
    sql = (
        "SELECT "
        "name, "
        "WHERE "
        "user_id = ?"
        "AND type = ?"
        "AND date = ?"
    )
# update_food_database.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'food.db'
FOOD_DB = sqlite3.connect(DB_FILE)
FOOD_DB.row_factory = sqlite3.Row

def get_food_version() -> int:
    """Returns food database version"""
    try:
        cur = FOOD_DB.cursor()
        cur.execute('PRAGMA user_version')
        record = cur.fetchone()
        return int(dict(record)['user_version'])
    except sqlite3.Error as error:
        print(f'Error: {error}')

if __name__ == '__main__':
    cur = FOOD_DB.cursor()
    db_version = get_food_version()
    sql = (
        "CREATE TABLE food "
        "(id INTEGER UNIQUE PRIMARY KEY NOT NULL, "
        "name TEXT NOT NULL, "
        "serving_size TEXT NOT NULL, "
        "calories INT NOT NULL, "
        "fat INT NOT NULL, "
        "cholesterol INT NOT NULL, "
        "sodium INT NOT NULL, "
        "carbs INT NOT NULL, "
        "protein INT NOT NULL, "
        "micronutrients TEXT "
        ")"
    )
    cur.execute(sql)
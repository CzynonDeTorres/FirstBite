# food.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'food.db'
FOOD_DB = sqlite3.connect(DB_FILE)
FOOD_DB.row_factory = sqlite3.Row

def add_new_food(**kwargs):
    cur = FOOD_DB.cursor()
    
    new_row = ''
    for values in kwargs.values():
        new_row += f'"{values}", '
    new_row = new_row[:len(new_row)-2]

    sql = (
        "INSERT INTO food (name, serving_size, calories, fat, cholesterol, sodium, carbs, protein, micronutrients)"
        "VALUES "
        f'({new_row});'
    )
    cur.executescript(sql)

def search_food():
    sql = (
        "SELECT "
        "name, serving_size, calories "
        "FROM food"
        "WHERE name LIKE '%?%'"
    )
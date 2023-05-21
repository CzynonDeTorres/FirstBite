# user.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'user.db'
FIRSTBITE_DB = sqlite3.connect(DB_FILE)
FIRSTBITE_DB.row_factory = sqlite3.Row

def create_users_meals():
    cur = FIRSTBITE_DB.cursor()
    attachSQL = "ATTACH DATABASE ? AS food "
    food_db = (f'{CURRENT_DIR}\\food.db',)
    cur.execute(attachSQL, food_db)
    sql = (
        "CREATE TABLE users "
        "(id INT UNIQUE PRIMARY KEY NOT NULL,"
        "name TEXT NOT NULL, "
        "height FLOAT NOT NULL, "
        "weight FLOAT NOT NULL, "
        "measurement_type INT NOT NULL, "
            # 1 - metric (cm, kg)
            # 2 - imperial (feet and inches, lbs)
        "bmi FLOAT NOT NULL, "
        "goals INT, "
            # 1 - lose weight
            # 2 - maintain weight
            # 3 - gain weight
        "activity_level INT, "
            # 1 - not very active
            # 2 - lightly active
            # 3 - active
            # 4 - very active
        "sex INT NOT NULL, "
            # 1 - cisgender male
            # 2 - cisgender female
            # 3 - queer
        "choices INT NOT NULL DEFAULT (0), "
            # 0 - not queer
            # 1 - has done gender-affirming medication or care (shortening to GAMC for convenience) to be male / has not done GAMC and is assigned male at birth
            # 2 - has done GAMC to be female / has not done GAMC and is assigned female at birth
        "birthday DATE, "
        "goal_weight FLOAT"
        ") "

        "CREATE TABLE meals "
        "(id INT UNIQUE PRIMARY KEY NOT NULL,"
        "type INT NOT NULL, "
            # 1 - breakfast
            # 2 - lunch
            # 3 - dinner
            # 4 - snack
        "name TEXT, "
        "user_id INT FOREIGN KEY REFERENCES users(id), "
        "food_id INT FOREIGN KEY REFERENCES food.food(id), "
        "date DATE"
        ")"
    )
    try:
        cur.execute(sql)
    except sqlite3.Error as error:
        print(error)
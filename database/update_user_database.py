# update_user_database.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'FirstBite.db'
FIRSTBITE_DB = sqlite3.connect(DB_FILE)
FIRSTBITE_DB.row_factory = sqlite3.Row
FIRSTBITE_DB.attach("food", "food.db")

cur = FIRSTBITE_DB.cursor()

if (not DB_FILE.is_file()):
    create_users_meals = (
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
        ")"

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

    cur.execute(create_users_meals)
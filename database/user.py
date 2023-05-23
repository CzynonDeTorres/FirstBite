# user.py

import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'user.db'
USER_DB = sqlite3.connect(DB_FILE)
USER_DB.row_factory = sqlite3.Row

# creates user.db file and users and meals tables in it
def create_users_meals():
    cur = USER_DB.cursor()
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
        "); "

        "CREATE TABLE meals "
        "(id INT UNIQUE PRIMARY KEY NOT NULL,"
        "type INT NOT NULL, "
            # 1 - breakfast
            # 2 - lunch
            # 3 - dinner
            # 4 - snack
        "user_id INT, "
        "food_id INT, "
        "name TEXT, "
        "date TEXT NOT NULL, "
        # TODO: since referencing other databases doesn't work in sqlite
        #       make a way to manually check food_id from other database
        "FOREIGN KEY(user_id) REFERENCES users(id) "
        ")"
    )
    try:
        cur.executescript(sql)
    except sqlite3.Error as error:
        print(error)

# adds a new user to the database
def add_new_user(**kwargs):
    cur = USER_DB.cursor()
    new_row = ''

    for values in kwargs.values():
        new_row += f'"{values}", '
    new_row = new_row[:len(new_row)-2]
    sql = (
        "INSERT INTO users (name, height, weight, measurement_type, bmi, goals, activity_level, sex, choices, birthday, goal_weight) "
        "VALUES "
        f'({new_row});'
    )
    try:
        cur.executescript(sql)
    except sqlite3.Error as error:
        print(error)
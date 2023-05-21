# main python file for FirstBite

import sqlite3
from sqlite3 import Error
from database import food, user as DB_USER
from pathlib import Path

try:
    user_db = Path(__file__) / 'database' / 'user.db'
    if not user_db.is_file():
        DB_USER.create_users_meals()
except Error as error:
    print(f'{error}')
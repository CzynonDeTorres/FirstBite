# main python file for FirstBite

import sqlite3
from sqlite3 import Error
from pathlib import Path

from database import food, user as DB_USER
from resources import start

# checks if there is a user database in database folder
try:
    user_db = Path(__file__) / 'database' / 'user.db'
    if not user_db.is_file():
        DB_USER.create_users_meals()
except Error as error:
    print(f'{error}')

if __name__ == "__main__":
    start.main()
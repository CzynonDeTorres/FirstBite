# food.py

import sqlite3
from pathlib import Path
from tabulate import tabulate

CURRENT_DIR = Path(__file__).parent
DB_FILE = CURRENT_DIR / 'food.db'
FOOD_DB = sqlite3.connect(DB_FILE)

class Food:
    def __init__(self):
        self.name = ""
        self.serving_size = ""
        self.calories = 0
        self.fat = 0
        self.cholesterol = 0
        self.sodium = 0
        self.carbs = 0
        self.protein = 0
        
    def add_new_food(**kwargs):
        cur = FOOD_DB.cursor()
        
        new_row = ''
        for values in kwargs.values():
            new_row += f'"{values}", '
        new_row = new_row[:len(new_row)-2]

        sql = (
            "INSERT INTO food (name, serving_size, calories, fat, cholesterol, sodium, carbs, protein)"
            "VALUES "
            f'({new_row});'
        )
        cur.executescript(sql)

    def search_food(self, food):
        sql = (
            "SELECT "
            "id, name, serving_size, calories "
            "FROM food "
            f'WHERE name LIKE "%{food}%"'
        )
        cur = FOOD_DB.cursor()
        cur.execute(sql)
        list_of_food = cur.fetchall()
        print(list_of_food)
        print(tabulate(list_of_food, headers=["ID", "Name", "Serving Size", "Calories"]))

    def set_food(self, id):
        sql = (
            "SELECT * "
            "FROM food "
            f'WHERE id CONTAINS "{id}"'
        )
        cur = FOOD_DB.cursor()
        cur.execute(sql)
        food_details = cur.fetchall()
        food_details = food_details[0]
        self.name = food_details[0]
        self.serving_size = food_details[1]
        self.calories = food_details[2]
        self.fat = food_details[3]
        self.cholesterol = food_details[4]
        self.sodium = food_details[5]
        self.carbs = food_details[6]
        self.protein = food_details[7]

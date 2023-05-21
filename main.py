# main python file for FirstBite

import sqlite3
from sqlite3 import Error
from database import food

print(dir(food))
food_data = {
    "name": 'Hansel Chocolate Sandwich Cream-Filled Biscuits',
    "serving_size": '31g per pack',
    "calories": '160',
    "fat": '7',
    "cholesterol": '0',
    "sodium": '85',
    "carbs": '21',
    "protein": '2',
    "micronutrients": 'Calcium: 14mg\nIron: 1mg'
}
food.add_new_food(**food_data)
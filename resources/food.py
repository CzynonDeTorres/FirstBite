# food.py
"""Contains everything related to adding, listing food"""

import sqlite3
from database import food as food_db

class Food():
    """object representing food"""
    id: int
    name: str
    serving_size: str
    calories: int
    fat: int
    cholesterol: int
    sodium: int
    carbs: int
    protein: int
    micronutrients: str

def new_food(self, **kwargs):
    self.name = kwargs.get('name')
    self.serving_size = kwargs.get('serving_size')
    self.calories = kwargs.get('calories')
    self.fat = kwargs.get('fat')
    self.cholesterol = kwargs.get('cholesterol')
    self.sodium = kwargs.get('sodium')
    self.carbs = kwargs.get('carbs')
    self.protein = kwargs.get('protein')
    self.micronutrients = kwargs.get('micronutrients', '')

    print(self)

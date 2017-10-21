"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato','mushroom'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato','mushroom'}

# The calories for each food item (a dictionary, where
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom':7
}

# Implement Food class here

class Food:
    __slots__ = ("name","is_veg","cal")

    def __init__( self,name):
        self.name = name
        self.is_veg = name in VEGGIES
        self.cal = CALORIES[self.name]

    def is_veggie(self):
        return self.is_veg

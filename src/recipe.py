from src.foods import Foods
from src.ingredient import Ingredient


class Recipe:
    def __init__(self, text, foods: Foods):
        self.foods = foods
        self.ingredients = [Ingredient(row, foods) for row in text]


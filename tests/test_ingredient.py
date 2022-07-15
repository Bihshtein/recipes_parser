import unittest
from ingredient import Ingredient

class TestIngredient(unittest.TestCase):
    def test_simple(self):
        ingredient = Ingredient('4 slices bread, cubed')
        self.assertEquals('4', ingredient.quantity)
        self.assertEquals('slices', ingredient.measure_size)
        self.assertEquals('cubed', ingredient.serving_form)
        self.assertEquals(['bread'], ingredient.ingredient)
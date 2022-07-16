import unittest
from src.foods import Foods
from pathlib import Path
from src.recipe import Recipe
import os


class TestFoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_folder = Path(__file__).absolute().parent
        cls.foods = Foods(folder=os.path.join(cls.test_folder, 'data')
)

    def setUp(self) -> None:
        self.foods = TestFoods.foods
        self.test_folder = TestFoods.test_folder

    def test_simple(self):
        filename = os.path.join(self.test_folder,  'data', 'test_recipe.txt')
        with open(filename) as file:
            lines = file.readlines()
        recipe = Recipe(foods=self.foods, text=lines)
        self.assertEquals(6, len(recipe.ingredients))
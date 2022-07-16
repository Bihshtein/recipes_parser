import unittest
from foods import Foods
from pathlib import Path
import os


class TestFoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        test_folder = Path(__file__).absolute().parent.parent
        cls.foods = Foods(folder=os.path.join(test_folder, 'data')
)

    def setUp(self) -> None:
        self.foods = TestFoods.foods

    def test_simple(self):
        food_item = self.foods.get_food_item(['raw', 'Tomatoes'])
        self.assertEquals('Tomatoes, yellow, raw', food_item)
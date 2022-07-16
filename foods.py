import os
import pandas as pd


class Foods:

    def __init__(self, folder):

        food_nutrient_path = os.path.join(folder, 'food_nutrient.csv')
        self.food_nutrient_df = pd.read_csv(food_nutrient_path)

        food_path= os.path.join(folder, 'food.csv')
        self.food_df = pd.read_csv(food_path).dropna(subset=['description'])
        nutrient_path= os.path.join(folder, 'nutrient.csv')
        self.nutrient_df = pd.read_csv(nutrient_path)
        #nutrient_df.query('name=="Sodium, Na"')

    def get_food_item(self, ingredient: list[str]):
        query = ''
        for word_index in range(len(ingredient)):
            query += f'description.str.contains("{ingredient[word_index]}")'
            if word_index < len(ingredient) - 1:
                query += ' & '

        return self.food_df.query(query).iloc[0]['description']

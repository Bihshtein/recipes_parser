import os
import pandas as pd


class Foods:

    def __init__(self, folder):

        self.food_df = pd.read_csv(os.path.join(folder, 'food.csv'))\
            .dropna(subset=['description'])

    def get_food_item(self, ingredient: list[str]):
        query = ''
        for word_index in range(len(ingredient)):
            query += f'description.str.contains("{ingredient[word_index]}")'
            if word_index < len(ingredient) - 1:
                query += ' & '

        return self.food_df.query(query).iloc[0]

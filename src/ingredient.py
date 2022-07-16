from src.foods import Foods
QUANTITY_KEYWORDS = ['slices', 'cup', 'cups', 'large', 'teaspoon']
SERVING_FORM_KEYWORDS = ['melted', 'cubed', 'beaten', 'shredded', 'chopped']

class Ingredient:

    def __init__(self, description : str, foods: Foods):
        words = description.strip().replace(',','').split(' ')
        self.quantity = words[0]
        self.measure_size  = words[1] if words[1] in QUANTITY_KEYWORDS else None
        self.serving_form = None
        for word_index in range(2, len(words)):
            if words[word_index] in SERVING_FORM_KEYWORDS:
                self.serving_form = words[word_index]
                del words[word_index]
                if self.measure_size:
                    self.ingredient = words[2:]
                else:
                    self.ingredient = words[1:]
                break
        if foods:
            food_item = foods.get_food_item(self.ingredient)
            self.matched_food_item = food_item['description']
            self.matched_food_fdc_id = food_item['fdc_id']

QUANTITY_KEYWORDS = ['slices', 'cup', 'cups', 'large', 'teaspoon']
SERVING_FORM_KEYWORDS = ['melted', 'cubed', 'beaten', 'shredded', 'teaspoon']

class Ingredient:

    def __init__(self, description : str):
        words = description.strip().replace(',','').split(' ')
        self.quantity = words[0]
        self.measure_size  = words[1] if words[1] in QUANTITY_KEYWORDS else None
        self.serving_form = None
        for word_index in range(2, len(words)):
            if words[word_index] in SERVING_FORM_KEYWORDS:
                self.serving_form = words[word_index]
                del words[word_index]
                self.ingredient = words[2:]

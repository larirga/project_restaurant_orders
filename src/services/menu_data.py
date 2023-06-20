import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, 'r') as csv_file:
            self.dishes = set()
            reader_dict = csv.DictReader(csv_file)
            for row in reader_dict:
                dishes_name = row['dish']
                dishes_price = float(row['price'])
                dishes_recipe = int(row['recipe_amount'])
                dishes_ingredient = row['ingredient']
                # add next dish to list
                self.dishes.add(Dish(dishes_name, dishes_price))

                later_dish = next(iter(self.dishes))

                later_dish.add_ingredient_dependency(
                    Ingredient(dishes_ingredient), dishes_recipe,
                )

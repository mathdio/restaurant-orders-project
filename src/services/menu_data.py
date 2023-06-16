# Req 3
import pandas as pd

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        dishes = set()

        menu_df = pd.read_csv(source_path)
        for dish in menu_df.groupby("dish"):
            name, df = dish
            price = df.iloc[0]["price"]
            dish_instance = Dish(name, price)

            for _, ingredient in df.iterrows():
                ingredient_instance = Ingredient(ingredient["ingredient"])
                amount = ingredient["recipe_amount"]
                dish_instance.add_ingredient_dependency(
                    ingredient_instance, amount
                )
                print(dish_instance.get_ingredients())


menu = MenuData("tests/mocks/menu_base_data.csv")

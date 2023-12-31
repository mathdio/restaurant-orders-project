import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def generate_dataframe(self, dishes):
        menu = []
        for dish in dishes:
            menu.append(
                {
                    "dish_name": dish.name,
                    "ingredients": dish.get_ingredients(),
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                }
            )
        return pd.DataFrame(menu)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        menu = set()
        print(self.inventory.inventory)
        for dish in self.menu_data.dishes:
            if (
                not restriction or restriction not in dish.get_restrictions()
            ) and (self.inventory.check_recipe_availability(dish.recipe)):
                self.inventory.consume_recipe(dish.recipe)
                menu.add(dish)
        return self.generate_dataframe(menu)


builder = MenuBuilder()
builder.get_main_menu()

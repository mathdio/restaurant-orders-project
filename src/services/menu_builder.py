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
        menu = {
            "dish_name": [],
            "ingredients": [],
            "price": [],
            "restrictions": [],
        }
        for dish in dishes:
            menu["dish_name"].append(dish.name)
            menu["price"].append(dish.price)

            for ingredient in dish.get_ingredients():
                menu["ingredients"].append(ingredient.name)
            for restriction in dish.get_restrictions():
                menu["restrictions"].append(restriction.name)
        print(menu)
        return dishes

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        if restriction is None:
            self.generate_dataframe(self.menu_data.dishes)
        else:
            dinamic_menu = set()
            for dish in self.menu_data.dishes:
                if restriction not in [
                    restr.name for restr in dish.get_restrictions()
                ]:
                    dinamic_menu.add(dish)
            return pd.DataFrame(dinamic_menu)


builder = MenuBuilder()
print(builder.get_main_menu())
# print(builder.get_main_menu("LACTOSE"))
# print(builder.get_main_menu("ANIMAL_MEAT"))

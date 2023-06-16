from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    pasta = Dish("pasta", 15.00)
    assert pasta == Dish("pasta", 15.00)
    assert pasta.name == "pasta"
    assert repr(pasta) == "Dish('pasta', R$15.00)"
    assert hash(pasta) == hash(Dish("pasta", 15.00))
    assert hash(pasta) != hash(Dish("meat", 20.00))

    meat = Ingredient("carne")
    pasta.add_ingredient_dependency(meat, 1)
    assert pasta.recipe == {meat: 1}

    assert pasta.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert pasta.get_ingredients() == {meat}

    with pytest.raises(TypeError):
        Dish("cake", "1")

    with pytest.raises(ValueError):
        Dish("cake", 0)

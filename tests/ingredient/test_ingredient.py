from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    meat = Ingredient("carne")
    assert meat == Ingredient("carne")
    assert meat.name == "carne"
    assert meat.__repr__() == "Ingredient('carne')"
    assert meat.__hash__() == Ingredient("carne").__hash__()
    assert meat.__hash__() != Ingredient("ovo").__hash__()
    assert meat.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

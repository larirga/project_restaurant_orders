import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish1 = Dish('lasanha', 25.90)
    dish2 = Dish('salmão', 30.0)
    ingredient1 = Ingredient('presunto')
    ingredient2 = Ingredient('queijo mussarela')

    assert dish1 == dish1
    assert dish1 != dish2
    assert dish1.name == 'lasanha'
    assert dish2.name == 'salmão'
    assert dish1.price == 25.90
    assert hash(dish1) == hash("Dish('lasanha', R$25.90)")
    assert repr(dish1) == "Dish('lasanha', R$25.90)"

    dish1.add_ingredient_dependency(ingredient1, 15)
    dish1.add_ingredient_dependency(ingredient2, 15)

    assert dish1.recipe == {ingredient1: 15, ingredient2: 15}
    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    with pytest.raises(TypeError):
        Dish('lasanha', '25.90')

    with pytest.raises(ValueError):
        Dish('lasanha', -25.90)

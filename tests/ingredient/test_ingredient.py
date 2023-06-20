from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('frango')
    ingredient3 = Ingredient('')

    assert ingredient == ingredient
    assert ingredient != ingredient2
    assert ingredient3.name == ''
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions

    assert hash(ingredient) == hash(ingredient)
    assert hash(ingredient) != hash(ingredient2)
    assert repr(ingredient) == "Ingredient('queijo mussarela')"

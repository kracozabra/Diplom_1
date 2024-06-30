import pytest

from praktikum.ingredient import Ingredient
from tests import data


class TestIngredient:

    @pytest.mark.parametrize('price', data.correct_ingredient_prices)
    def test_get_price_positive(self, price):
        ingredient = Ingredient('SAUCE', 'Ketchup', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', data.correct_ingredient_names)
    def test_get_name_positive(self, name):
        ingredient = Ingredient('SAUCE', name, 0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('types', data.correct_ingredient_types)
    def test_get_type_positive(self, types):
        ingredient = Ingredient(types, 'Cheese', 0)
        assert ingredient.get_type() == types

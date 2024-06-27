import pytest

from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from tests import data


class TestBurger:

    def test_set_buns_positive(self):
        burger = Burger()
        burger.set_buns(data.correct_bun)
        assert burger.bun.name == data.correct_bun.get_name()

    @pytest.mark.parametrize('ingredient', data.correct_ingredients)
    def test_add_ingredient_positive(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_positive(self):
        burger = Burger()
        burger.ingredients = data.correct_ingredients.copy()
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == len(data.correct_ingredients) - 1
        assert data.correct_ingredients[0] not in burger.ingredients

    def test_move_ingredient_positive(self):
        burger = Burger()
        burger.ingredients = data.correct_ingredients.copy()
        burger.move_ingredient(1, 0)
        print(burger.ingredients[0].name)
        assert burger.ingredients[0] == data.correct_ingredients[1]

    def test_get_price_positive(self):
        burger = Burger()
        burger.ingredients = data.correct_ingredients.copy()
        burger.bun = data.correct_bun
        expecting_result = sum([el.price for el in data.correct_ingredients]) + data.correct_bun.price * 2
        assert burger.get_price() == expecting_result

    def test_burger_get_receipt_positive(self):
        burger = Burger()
        burger.bun = data.correct_bun
        burger.ingredients = data.correct_ingredients.copy()
        receipt = burger.get_receipt()
        assert (burger.bun.name in receipt) and [el.name in receipt for el in data.correct_ingredients]

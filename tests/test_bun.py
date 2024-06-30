import pytest

from praktikum.bun import Bun
from tests import data


class TestBun:

    @pytest.mark.parametrize('name', data.correct_bun_names)
    def test_get_name_positive(self, name):
        bun = Bun(name, 0)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', data.correct_bun_prices)
    def test_get_price_positive(self, price):
        bun = Bun('Bun', price)
        assert bun.get_price() == price

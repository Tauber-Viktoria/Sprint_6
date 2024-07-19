import pytest
from data import data_sets


class TestOrderPage:
    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_first_form(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()

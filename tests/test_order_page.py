import time

import pytest
from data import data_sets


class TestOrderPage:
    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_first_form(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        assert order_page.find_order_button(), "кнопка 'Заказать' не найдена на странице"

    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_all_form(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        order_page.set_second_form(data_set)
        order_page.click_to_order_button()
        assert order_page.find_assert_button(), "модальное окно с подверждением заказа не найдено на странице"

    @pytest.mark.parametrize("data_set", data_sets)
    def test_create_order(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        order_page.set_second_form(data_set)
        order_page.click_to_order_button()
        order_page.click_to_accept_order_button()
        assert order_page.find_order_modal(), ("модальное окно с сообщением об успешном создании заказа не найдено на "
                                               "странице")

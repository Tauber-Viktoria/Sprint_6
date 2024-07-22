import pytest

import URL
from data import data_sets


class TestOrderPage:
    def test_switch_to_yandex_site(self, order_page):
        current_url = order_page.switch_to_yandex_site()
        assert "dzen.ru" in current_url, "не открылась главная страница Дзена."

    def test_switch_to_main_page(self, order_page):
        current_url = order_page.switch_to_main_page()
        assert current_url == URL.MAIN_URL, "не произошел переход на главную страницу «Самоката»."

    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_first_form(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        assert order_page.find_order_button(), "кнопка 'Заказать' не найдена на странице"

    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_all_forms(self, order_page, data_set):
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

import pytest
import allure
import URL
from data import data_sets


class TestOrderPage:
    @allure.feature('Переходы на внешние сайты')
    @allure.story('Переход на главную страницу Дзена')
    @allure.title('Тест перехода на главную страницу Дзена при клике на логотип Яндекса')
    def test_switch_to_yandex_site(self, order_page):
        current_url = order_page.switch_to_yandex_site()
        assert "dzen.ru" in current_url, "не открылась главная страница Дзена."

    @allure.feature('Переходы на страницы')
    @allure.story('Переход на главную страницу «Самоката»')
    @allure.title('Тест перехода на главную страницу «Самоката» при клике на логотип «Самокат»')
    def test_switch_to_main_page(self, order_page):
        current_url = order_page.switch_to_main_page()
        assert current_url == URL.MAIN_URL, "не произошел переход на главную страницу «Самоката»."

    @allure.feature('Формы заказа')
    @allure.story('Заполнение первой формы')
    @allure.title('Тест заполнения первой формы заказа')
    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_first_form(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        assert order_page.find_order_button(), "кнопка 'Заказать' не найдена на странице"

    @allure.feature('Формы заказа')
    @allure.story('Заполнение всех форм')
    @allure.title('Тест заполнения всех форм заказа')
    @pytest.mark.parametrize("data_set", data_sets)
    def test_fill_all_forms(self, order_page, data_set):
        order_page.click_to_cookie_button()
        order_page.set_first_form(data_set)
        order_page.click_to_next_button()
        order_page.set_second_form(data_set)
        order_page.click_to_order_button()
        assert order_page.find_assert_button(), "модальное окно с подверждением заказа не найдено на странице"

    @allure.feature('Формы заказа')
    @allure.story('Создание заказа')
    @allure.title('Тест создания заказа')
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

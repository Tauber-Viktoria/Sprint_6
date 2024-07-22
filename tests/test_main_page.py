import pytest
import allure
import URL
from data import ANSWERS


class TestMainPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу оформления заказа из хедера')
    @allure.title('Тест перехода на страницу оформления заказа по клику на кнопку "Заказать" в хедере')
    def test_switch_to_order_page_click_on_header_button(self, main_page):
        main_page.click_to_cookie_button()
        current_url = main_page.click_header_order_button()
        assert current_url == URL.ORDER_URL, ("не произошел переход на страницу оформления заказа по клику на кнопку "
                                              "'Заказать' в хедере")

    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу оформления заказа с главной страницы')
    @allure.title('Тест перехода на страницу оформления заказа по клику на кнопку "Заказать" на главной странице')
    def test_switch_to_order_page_click_on_button(self, main_page):
        main_page.click_to_cookie_button()
        main_page.execute_scroll()
        current_url = main_page.click_order_button()
        assert current_url == URL.ORDER_URL, ("не произошел переход на страницу оформления заказа по клику на кнопку "
                                              "'Заказать' на главной странице")

    @allure.feature('Вопросы и ответы')
    @allure.story('Проверка отображения ответов на вопросы')
    @allure.title('Тест отображения ответа на вопрос {q_num}')
    @pytest.mark.parametrize(
        "q_num, expected_result",
        [(i, ANSWERS.get(i)) for i in range(8)]
    )
    def test_click_to_questions_show_answers(self, main_page, q_num, expected_result):
        main_page.click_to_cookie_button()
        main_page.execute_scroll()
        main_page.click_to_question(q_num)
        result = main_page.get_answer_text(q_num)
        assert result == expected_result, 'Ответ на вопрос не совпадает с ожидаемым значением.'

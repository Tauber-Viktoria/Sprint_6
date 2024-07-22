import pytest

import URL
from data import ANSWERS


class TestMainPage:
    def test_switch_to_order_page_click_on_header_button(self, main_page):
        main_page.click_to_cookie_button()
        current_url = main_page.click_header_order_button()
        assert current_url == URL.ORDER_URL

    def test_switch_to_order_page_click_on_button(self, main_page):
        main_page.click_to_cookie_button()
        main_page.execute_scroll()
        current_url = main_page.click_order_button()
        assert current_url == URL.ORDER_URL

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

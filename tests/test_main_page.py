import pytest

from data import ANSWERS


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num, expected_result",
        [(i, ANSWERS.get(i)) for i in range(8)]
    )
    def test_questions(self, main_page, q_num, expected_result):
        main_page.click_to_cookie_button()
        main_page.execute_scroll()
        main_page.click_to_question(q_num)
        result = main_page.get_answer_text(q_num)
        assert result == expected_result

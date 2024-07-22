from locators.MainPageLocators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Заказать' в хедере страницы и перейти на оформление заказа")
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)
        return self.get_current_url()

    @allure.step("Кликнуть на кнопку 'Заказать' на главной странице и перейти на оформление заказа")
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)
        return self.get_current_url()

    @allure.step("Принять куки")
    def click_to_cookie_button(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Прокрутить до вопросов")
    def execute_scroll(self):
        element = self.find_element_with_wait(MainPageLocators.SUB_HEADER_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на вопрос {num}")
    def click_to_question(self, num):
        method, locator_template = MainPageLocators.QUESTION_LOCATOR
        locator = (method, locator_template.format(num))
        self.click_on_element(locator)

    @allure.step("Получить ответ на вопрос {num}")
    def get_answer_text(self, num):
        method, locator_template = MainPageLocators.ANSWER_LOCATOR
        locator = (method, locator_template.format(num))
        return self.get_text_from_element(locator)

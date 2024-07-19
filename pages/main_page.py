from locators.MainPageLocators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_to_cookie_button(self, locator):
        self.find_element_with_wait(MainPageLocators.COOKIE_BUTTON)
        self.click_on_element(locator)

    def execute_scroll(self):
        element = self.find_element_with_wait(MainPageLocators.SUB_HEADER_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_to_question(self, num):
        method, locator_template = MainPageLocators.QUESTION_LOCATOR
        locator = (method, locator_template.format(num))
        self.click_on_element(locator)

    def get_answer_text(self, num):
        method, locator_template = MainPageLocators.ANSWER_LOCATOR
        locator = (method, locator_template.format(num))
        return self.get_text_from_element(locator)




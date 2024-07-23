from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, URL):
        self.driver.get(URL)

    def get_current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def switch_to_window_contains(self, partial_url):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(partial_url))
        return self.driver.current_url


from locators.OrderPageLocators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def click_to_cookie_button(self):
        self.click_on_element(OrderPageLocators.COOKIE_BUTTON)

    def set_first_name(self, first_name):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD).send_keys(first_name)

    def set_last_name(self, last_name):
        self.find_element_with_wait(OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.find_element_with_wait(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def choose_metro(self):
        self.find_element_with_wait(OrderPageLocators.METRO_FIELD).click()
        self.find_element_with_wait(OrderPageLocators.METRO_ELEMENT).click()

    def set_mobile_phone_number(self, mobile_phone_number):
        self.find_element_with_wait(OrderPageLocators.MOBILE_PHONE_FIELD).send_keys(mobile_phone_number)

    def click_to_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def set_first_form(self, data):
        self.set_first_name(data['first_name'])
        self.set_last_name(data['last_name'])
        self.set_address(data['address'])
        self.choose_metro()
        self.set_mobile_phone_number(data['mobile_phone_number'])
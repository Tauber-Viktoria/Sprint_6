import time

from selenium.webdriver.common.by import By

from locators.OrderPageLocators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):

    def click_to_cookie_button(self):
        self.click_on_element(OrderPageLocators.COOKIE_BUTTON)

    def set_first_name(self, first_name):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD).send_keys(first_name)

    def set_last_name(self, last_name):
        self.find_element_with_wait(OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.find_element_with_wait(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def choose_metro(self, metro):
        self.find_element_with_wait(OrderPageLocators.METRO_FIELD).click()
        metro_locator = self.get_metro_element_locator(metro)
        self.find_element_with_wait(metro_locator).click()

    @staticmethod
    def get_metro_element_locator(metro):
        method, locator_template = OrderPageLocators.METRO_ELEMENT
        locator = (method, locator_template.format(metro))
        return locator

    def set_mobile_phone_number(self, mobile_phone_number):
        self.find_element_with_wait(OrderPageLocators.MOBILE_PHONE_FIELD).send_keys(mobile_phone_number)

    def click_to_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def set_first_form(self, data):
        self.set_first_name(data['first_name'])
        self.set_last_name(data['last_name'])
        self.set_address(data['address'])
        self.choose_metro(data['metro'])
        self.set_mobile_phone_number(data['mobile_phone_number'])

    def find_order_button(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    def set_rental_date(self, rental_date):
        self.find_element_with_wait(OrderPageLocators.RENTAL_DATE_FIELD).send_keys(rental_date)

    def choose_rental_period(self, rental_period):
        self.find_element_with_wait(OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        rental_option_locator = self.get_rental_date_element_locator(rental_period)
        self.find_element_with_wait(rental_option_locator).click()

    @staticmethod
    def get_rental_date_element_locator(rental_period):
        method, locator_template = OrderPageLocators.RENTAL_PERIOD_ELEMENT
        locator = (method, locator_template.format(rental_period))
        return locator

    def choose_scooter_color(self, scooter_colors):
        for color in scooter_colors:
            color_checkbox = self.get_scooter_color_checkbox(color)
            self.find_element_with_wait(color_checkbox).click()

    @staticmethod
    def get_scooter_color_checkbox(color):
        method, locator_template = OrderPageLocators.SCOOTER_COLOR_CHECKBOX
        locator = (method, locator_template.format(color))
        return locator

    def set_comment(self, comment):
        self.find_element_with_wait(OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    def set_second_form(self, data):
        self.set_rental_date(data['rental_date'])
        self.choose_rental_period(data['rental_period'])
        self.choose_scooter_color(data['scooter_color'])
        self.set_comment(data['comment'])

    def click_to_order_button(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON).click()

    def find_assert_button(self):
        return self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON)

    #def click_to_accept_order_button(self):
    #self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON).click()

from locators.OrderPageLocators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    @allure.step("Нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена")
    def switch_to_yandex_site(self):
        self.click_on_element(OrderPageLocators.YANDEX_SITE_BUTTON)
        return self.switch_to_window_contains("dzen.ru")

    @allure.step("Нажать на логотип «Самоката» и перейти на главную страницу «Самоката")
    def switch_to_main_page(self):
        self.click_on_element(OrderPageLocators.MAIN_PAGE_BUTTON)
        return self.get_current_url()

    @allure.step("Принять куки")
    def click_to_cookie_button(self):
        self.click_on_element(OrderPageLocators.COOKIE_BUTTON)

    @allure.step('Ввод имени')
    def set_first_name(self, first_name):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD).send_keys(first_name)

    @allure.step('Ввод фамилии')
    def set_last_name(self, last_name):
        self.find_element_with_wait(OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.find_element_with_wait(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбор метро')
    def choose_metro(self, metro):
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        metro_locator = self.get_metro_element_locator(metro)
        self.click_on_element(metro_locator)

    @staticmethod
    def get_metro_element_locator(metro):
        method, locator_template = OrderPageLocators.METRO_ELEMENT
        locator = (method, locator_template.format(metro))
        return locator

    @allure.step('Ввод номера телефона')
    def set_mobile_phone_number(self, mobile_phone_number):
        self.find_element_with_wait(OrderPageLocators.MOBILE_PHONE_FIELD).send_keys(mobile_phone_number)

    @allure.step('Нажать "Далее"')
    def click_to_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def find_order_button(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ввод даты')
    def set_rental_date(self, rental_date):
        self.find_element_with_wait(OrderPageLocators.RENTAL_DATE_FIELD).send_keys(rental_date)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, rental_period):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_option_locator = self.get_rental_date_element_locator(rental_period)
        self.click_on_element(rental_option_locator)

    @staticmethod
    def get_rental_date_element_locator(rental_period):
        method, locator_template = OrderPageLocators.RENTAL_PERIOD_ELEMENT
        locator = (method, locator_template.format(rental_period))
        return locator

    @allure.step('Выбор цвета')
    def choose_scooter_color(self, scooter_colors):
        for color in scooter_colors:
            color_checkbox = self.get_scooter_color_checkbox(color)
            self.click_on_element(color_checkbox)

    @staticmethod
    def get_scooter_color_checkbox(color):
        method, locator_template = OrderPageLocators.SCOOTER_COLOR_CHECKBOX
        locator = (method, locator_template.format(color))
        return locator

    @allure.step('Ввод комментария для курьера')
    def set_comment(self, comment):
        self.find_element_with_wait(OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step('Нажать "Заказать"')
    def click_to_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    def find_assert_button(self):
        return self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON)

    @allure.step('Нажать "да" для подтверждения заказа')
    def click_to_accept_order_button(self):
        self.find_assert_button().click()

    def find_order_modal(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_MODAL)

    @allure.step('Ввести данные для первой формы заказа')
    def set_first_form(self, data):
        self.set_first_name(data['first_name'])
        self.set_last_name(data['last_name'])
        self.set_address(data['address'])
        self.choose_metro(data['metro'])
        self.set_mobile_phone_number(data['mobile_phone_number'])

    @allure.step('Ввести данные для второй формы заказа')
    def set_second_form(self, data):
        self.set_rental_date(data['rental_date'])
        self.choose_rental_period(data['rental_period'])
        self.choose_scooter_color(data['scooter_color'])
        self.set_comment(data['comment'])

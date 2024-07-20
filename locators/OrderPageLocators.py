from selenium.webdriver.common.by import By


class OrderPageLocators:
    COOKIE_BUTTON = (By.XPATH, ".//button[text()='да все привыкли']")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder,'метро')]")
    MOBILE_PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    METRO_ELEMENT = (By.XPATH, "//div[text()='{}']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")


from selenium.webdriver.common.by import By


class OrderPageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder,'метро')]")
    MOBILE_PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    METRO_ELEMENT = (By.XPATH, "//div[text()='{}']")
    RENTAL_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_ELEMENT = (By.XPATH, "//div[text()='{}']")
    SCOOTER_COLOR_CHECKBOX = (By.XPATH, "//input[@id='{}']")
    COMMENT_FIELD = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle__1CSJM') and text()='Заказать']")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    YANDEX_SITE_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    MAIN_PAGE_BUTTON = (By.XPATH, "//img[@alt='Scooter']")

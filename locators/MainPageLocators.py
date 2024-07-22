from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    ANSWER_LOCATOR = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    SUB_HEADER_LOCATOR = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    COOKIE_BUTTON = (By.XPATH,  '//*[@id="rcc-confirm-button"]')
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM') and text("
                              ")='Заказать']")

import pytest
from selenium import webdriver
from URL import MAIN_URL, ORDER_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_url(MAIN_URL)
    return page


@pytest.fixture()
def order_page(driver):
    page = OrderPage(driver)
    page.get_url(ORDER_URL)
    return page

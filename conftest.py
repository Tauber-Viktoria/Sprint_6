import pytest
from selenium import webdriver

from data import MAIN_URL
from pages.main_page import MainPage


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

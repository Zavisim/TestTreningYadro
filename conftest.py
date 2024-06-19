import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.careers_page import CareersPage


@pytest.fixture
def browser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def careers_page(browser) -> CareersPage:
    return CareersPage(browser)

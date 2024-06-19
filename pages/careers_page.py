import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base import BasePage


class CareersPage(BasePage):
    URL = "https://careers.yadro.com"

    @property
    def search(self):
        search = self.driver.find_element(By.CSS_SELECTOR, ".form-control")
        return search

    @property
    def butt_search(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".input-group-append")

    @property
    def result_search(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".vac__result-item-title")

    @property
    def result_search_name(self) -> list[str]:
        names = []
        for element in self.result_search:
            names.append(element.text)
        return names

    @property
    def butt_more(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.vac__result-more .btn')

    @property
    def butt_careers(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.vac__result-item-title')

    @property
    def careers_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.col-md')

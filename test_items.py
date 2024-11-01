import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestMultilang:
    test_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    def test_lang(self, browser):
        browser.get(self.test_page)
        els = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

        assert len(els) != 0, "Кнопка отстутсвует"

from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

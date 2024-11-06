from pages.main_page import MainPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


login_link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, login_link)
    page.open()
    page.should_be_login_link()

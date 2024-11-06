# from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# login_link = "http://selenium1py.pythonanywhere.com/"
# login_link = "https://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
login_link = "https://selenium1py.pythonanywhere.com/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, login_link)
    page.open()

    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

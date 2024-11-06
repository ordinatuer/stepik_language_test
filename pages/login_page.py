from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url

        _str = current_url.split("//")[1]
        _str = _str.split("/")
        _str.pop(1)

        if _str[-1] == "":
            _str.pop(-1)
        _str = "/".join(_str)

        assert LoginPageLocators.URL_PAGE_LOGIN == _str, "Invalid login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Register form not found"

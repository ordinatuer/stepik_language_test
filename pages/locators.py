from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")

    URL_PAGE_LOGIN = "selenium1py.pythonanywhere.com/accounts/login"

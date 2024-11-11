from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")

    URL_PAGE_LOGIN = "selenium1py.pythonanywhere.com/accounts/login"

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_TO_BASKET_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")
    BOOK_CARD_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_ADD_TO_BASKET_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    BOOK_CARD_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_ADD_TO_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

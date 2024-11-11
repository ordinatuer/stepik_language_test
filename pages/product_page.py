from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS), "Add to basket failed"

        name = self.compare_elements(
            ProductPageLocators.BOOK_CARD_NAME,
            ProductPageLocators.BOOK_ADD_TO_BASKET_NAME
        )
        price = self.compare_elements(
            ProductPageLocators.BOOK_CARD_PRICE,
            ProductPageLocators.BOOK_ADD_TO_BASKET_PRICE
        )

        assert name and price, "Add to basket success with errors"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        print(f"{answer}")
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def book_add_to_basket_correct(self):
        self.browser.find_element()

from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def compare_elements(self, el1, el2):
        el1_text = self.browser.find_element(*el1).text
        el2_text = self.browser.find_element(*el2).text

        return el1_text == el2_text

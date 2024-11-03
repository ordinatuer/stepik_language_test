from selenium import webdriver
import time
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Set language for testing"
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    time.sleep(5)
    browser.quit()

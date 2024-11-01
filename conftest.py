from selenium import webdriver
import time
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Set browser: Chrome or Edge"
    )
    parser.addoption(
        "--language",
        action="store",
        default="uk",
        help="Set language for testing"
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {'intl.accept_languages': language})

        browser = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("prefs", {'intl.accept_languages': language})

        browser = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError('--browser_name is "chrome" or "edge"')

    yield browser
    time.sleep(5)
    browser.quit()

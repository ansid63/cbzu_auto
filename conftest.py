import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser():
    # language = request.config.getoption("language")
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # capabilities = DesiredCapabilities.FIREFOX
    # remote_server = 'http://192.168.170.14:4445/wd/hub'
    # browser = webdriver.Remote(command_executor='http://192.168.170.14:4445/wd/hub', desired_capabilities={'browserName': 'firefox', 'platform': 'LINUX'})
    browser = webdriver.Remote(command_executor='localhost:4444/wd/hub',
                               desired_capabilities={'browserName': 'firefox'})

    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()
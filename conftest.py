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
    capabilities = DesiredCapabilities.CHROME
    remote_server = 'http://localhost:4444/wd/hub'
    browser = webdriver.Remote(remote_server, capabilities)


    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()
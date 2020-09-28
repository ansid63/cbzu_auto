import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})


    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()
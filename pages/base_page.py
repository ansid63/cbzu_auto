import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "http://musclegain.ru/calculator_bzu.html"

    def open(self):
        return self.browser.get(self.base_url)

    @allure.step("Нажать на кнопку {element}")
    def click_element(self, element):
        self.browser.find_element(element.search_method, element.locator).click()

    @allure.step("Дождаться состояния кликабельности элемента {element} в течении {timeout} сек.")
    def wait_element_clickable(self, element, timeout):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.element_to_be_clickable((element.search_method, element.locator)))

    @allure.step("Дождаться появления элемента {element} в течении {timeout} сек.")
    def wait_element_visible(self, element, timeout):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of_element_located((element.search_method, element.locator)))

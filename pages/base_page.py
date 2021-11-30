import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "http://musclegain.ru/calculator_bzu.html"
        self.browser.implicitly_wait(10)

    def open(self):
        return self.browser.get(self.base_url)

    @allure.step("Нажать на кнопку {locator_name}")
    def click_element(self, search_method, locator, locator_name):
        self.browser.find_element(search_method, locator).click()

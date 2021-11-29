class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "http://musclegain.ru/calculator_bzu.html"
        self.browser.implicitly_wait(10)

    def open(self):
        return self.browser.get(self.base_url)

    def click_element(self, *element):
        self.browser.find_element(*element).click()

from .base_page import BasePage
from .locators import BasePageLocators
from .data import TestData


class MainPage(BasePage):
    def send_text_to_field(self, text, *element):
        self.browser.find_element(*element).send_keys(text)

    def fill_value_positive(self):
        self.send_text_to_field(TestData.POS_AGE, *BasePageLocators.AGE)
        self.send_text_to_field(TestData.POS_HEIGHT, *BasePageLocators.HEIGHT)
        self.send_text_to_field(TestData.POS_WEIGHT, *BasePageLocators.WEIGHT)

        self.click_element(*BasePageLocators.GENDER)
        self.click_element(*BasePageLocators.TYPE)
        self.click_element(*BasePageLocators.VOLUME_ACTION)

        self.click_element(*BasePageLocators.SUBMIT)

    def fill_value_negative(self):
        self.send_text_to_field(TestData.POS_AGE, *BasePageLocators.AGE)
        self.send_text_to_field(TestData.POS_HEIGHT, *BasePageLocators.HEIGHT)
        self.send_text_to_field(TestData.NEGATIVE_WEIGHT, *BasePageLocators.WEIGHT)

        self.click_element(*BasePageLocators.GENDER)
        self.click_element(*BasePageLocators.TYPE)
        self.click_element(*BasePageLocators.VOLUME_ACTION)

        self.click_element(*BasePageLocators.SUBMIT)

    def check_numbers(self):
        number_charise = self.browser.find_element(*BasePageLocators.NUMBER_CHARIS_BENEDIKT).text
        assert (number_charise == '2421,42'), "Что то пошло не так у Харриса-Беннедикта"
        print("Верное число Харриса-Бенедикта в форме")

        number_bazal = self.browser.find_element(*BasePageLocators.NUMBER_BAZAL_META).text
        assert (number_bazal == '1837,89'), "Что то пошло не так у базальный метаболизм"
        print("Верное число базальный метаболизм в форме")

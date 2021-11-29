from .base_page import BasePage
from .locators import BasePageLocators
from .data import TestData


class MainPage(BasePage):
    def send_text_to_field(self, text, *element):
        self.browser.find_element(*element).send_keys(text)

    def fill_value_positive(self):
        # fill_age = self.browser.find_element(*BasePageLocators.AGE)
        # fill_age.send_keys(TestData.POS_AGE)
        self.send_text_to_field(TestData.POS_AGE, *BasePageLocators.AGE)
        # fill_height = self.browser.find_element(*BasePageLocators.HEIGHT)
        # fill_height.send_keys(TestData.POS_HEIGHT)
        self.send_text_to_field(TestData.POS_HEIGHT, *BasePageLocators.HEIGHT)
        # fill_weight = self.browser.find_element(*BasePageLocators.WEIGHT)
        # fill_weight.send_keys(TestData.POS_WEIGHT)
        self.send_text_to_field(TestData.POS_WEIGHT, *BasePageLocators.WEIGHT)

        self.click_element(*BasePageLocators.GENDER)
        # gender_choose.click()
        self.click_element(*BasePageLocators.TYPE)
        # type_choose.click()
        self.click_element(*BasePageLocators.VOLUME_ACTION)
        # volume_action.click()

        self.click_element(*BasePageLocators.SUBMIT)
        # submit_button.click()

    def fill_value_negative(self):
        self.send_text_to_field(TestData.POS_AGE, *BasePageLocators.AGE)
        # fill_age = self.browser.find_element(*BasePageLocators.AGE)
        # fill_age.send_keys(TestData.POS_AGE)
        self.send_text_to_field(TestData.POS_HEIGHT, *BasePageLocators.HEIGHT)
        # fill_height = self.browser.find_element(*BasePageLocators.HEIGHT)
        # fill_height.send_keys(TestData.POS_HEIGHT)
        self.send_text_to_field(TestData.NEGATIVE_WEIGHT, *BasePageLocators.WEIGHT)
        # fill_weight = self.browser.find_element(*BasePageLocators.WEIGHT)
        # fill_weight.send_keys(TestData.NEGATIVE_WEIGHT)

        self.click_element(*BasePageLocators.GENDER)
        # gender_choose.click()
        self.click_element(*BasePageLocators.TYPE)
        # type_choose.click()
        self.click_element(*BasePageLocators.VOLUME_ACTION)
        # volume_action.click()

        self.click_element(*BasePageLocators.SUBMIT)
        # submit_button.click()

    def check_numbers(self):
        number_charise = self.browser.find_element(*BasePageLocators.NUMBER_CHARIS_BENEDIKT).text
        assert (number_charise == '2421,42'), "Что то пошло не так у Харриса-Беннедикта"
        print("Верное число Харриса-Бенедикта в форме")

        number_bazal = self.browser.find_element(*BasePageLocators.NUMBER_BAZAL_META).text
        assert (number_bazal == '1837,89'), "Что то пошло не так у базальный метаболизм"
        print("Верное число базальный метаболизм в форме")

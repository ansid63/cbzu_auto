from .base_page import BasePage
from .locators import BasePageLocators
from data.data import TestData


class MainPage(BasePage):
    def fill_value_positive(self):
        fill_age = self.browser.find_element(*BasePageLocators.AGE)
        fill_age.send_keys(TestData.POS_AGE)
        fill_height = self.browser.find_element(*BasePageLocators.HEIGHT)
        fill_height.send_keys(TestData.POS_HEIGHT)
        fill_weight = self.browser.find_element(*BasePageLocators.WEIGHT)
        fill_weight.send_keys(TestData.POS_WEIGHT)

        gender_choose = self.browser.find_element(*BasePageLocators.GENDER)
        gender_choose.click()
        type_choose = self.browser.find_element(*BasePageLocators.TYPE)
        type_choose.click()
        volume_action = self.browser.find_element(*BasePageLocators.VOLUME_ACTION)
        volume_action.click()

        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT)
        submit_button.click()

    def fill_value_negative(self):
        fill_age = self.browser.find_element(*BasePageLocators.AGE)
        fill_age.send_keys(TestData.POS_AGE)
        fill_height = self.browser.find_element(*BasePageLocators.HEIGHT)
        fill_height.send_keys(TestData.POS_HEIGHT)
        fill_weight = self.browser.find_element(*BasePageLocators.WEIGHT)
        fill_weight.send_keys(TestData.NEGATIVE_WEIGHT)

        gender_choose = self.browser.find_element(*BasePageLocators.GENDER)
        gender_choose.click()
        type_choose = self.browser.find_element(*BasePageLocators.TYPE)
        type_choose.click()
        volume_action = self.browser.find_element(*BasePageLocators.VOLUME_ACTION)
        volume_action.click()

        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT)
        submit_button.click()

    def check_numbers(self):
        number_charise = self.browser.find_element(*BasePageLocators.NUMBER_CHARIS_BENEDIKT).text
        assert (number_charise == '2421,42'), "Что то пошло не так у Харриса-Беннедикта"
        print("Верное число Харриса-Бенедикта в форме")

        number_bazal = self.browser.find_element(*BasePageLocators.NUMBER_BAZAL_META).text
        assert (number_bazal == '1837,89'), "Что то пошло не так у базальный метаболизм"
        print("Верное число базальный метаболизм в форме")

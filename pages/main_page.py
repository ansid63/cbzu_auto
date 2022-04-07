import allure
from .base_page import BasePage
from .data import TestData
from .locators import *


class MainPage(BasePage):
    @allure.step("Заполнить поле {element} текстом {text}")
    def send_text_to_field(self, element, text):
        self.browser.find_element(element.search_method, element.locator).send_keys(text)

    def fill_value_positive(self):
        self.send_text_to_field(AGE_FIELD, TestData.POS_AGE)
        self.send_text_to_field(HEIGHT, TestData.POS_HEIGHT)
        self.send_text_to_field(WEIGHT, TestData.POS_WEIGHT)

        self.click_element(GENDER)
        self.click_element(TYPE)
        self.click_element(VOLUME_ACTION)
        self.click_element(SUBMIT)

    # def fill_value_negative(self):
    #     self.send_text_to_field(TestData.POS_AGE, NamedElement.AGE.search_method,
    #                             NamedElement.AGE.locator, NamedElement.AGE.locator_name)
    #     self.send_text_to_field(TestData.POS_HEIGHT, NamedElement.HEIGHT.search_method,
    #                             NamedElement.HEIGHT.locator, NamedElement.HEIGHT.locator_name)
    #     self.send_text_to_field(TestData.NEGATIVE_WEIGHT, NamedElement.WEIGHT.search_method,
    #                             NamedElement.WEIGHT.locator, NamedElement.WEIGHT.locator_name)
    #
    #     self.click_element(NamedElement.GENDER.search_method, NamedElement.GENDER.locator, NamedElement.GENDER.locator_name)
    #     self.click_element(NamedElement.TYPE.search_method, NamedElement.TYPE.locator, NamedElement.TYPE.locator_name)
    #     self.click_element(NamedElement.VOLUME_ACTION.search_method, NamedElement.VOLUME_ACTION.locator, NamedElement.VOLUME_ACTION.locator_name)
    #     self.click_element(NamedElement.SUBMIT.search_method, NamedElement.SUBMIT.locator, NamedElement.SUBMIT.locator_name)

    def check_numbers(self):
        number_charise = self.browser.find_element(NUMBER_CHARIS_BENEDIKT.search_method,
                                                   NUMBER_CHARIS_BENEDIKT.locator).text
        with allure.step("Проверяем число Харриса-Беннедикта"):
            assert (number_charise == '2421,42'), "Что то пошло не так у Харриса-Беннедикта"
        print("Верное число Харриса-Бенедикта в форме")

        number_bazal = self.browser.find_element(NUMBER_BAZAL_META.search_method,
                                                 NUMBER_BAZAL_META.locator).text
        with allure.step("Проверяем число базальный метаболизм"):
            assert (number_bazal == '1837,89'), "Что то пошло не так у базальный метаболизм"
        print("Верное число базальный метаболизм в форме")

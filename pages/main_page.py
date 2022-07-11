import allure
from .base_page import BasePage
from .data import TestData
from .locators import AGE_FIELD, HEIGHT, WEIGHT, GENDER, TYPE, VOLUME_ACTION, SUBMIT, NUMBER_BAZAL_META, \
    NUMBER_CHARIS_BENEDIKT


class MainPage(BasePage):
    @allure.step("Заполнить поле {element} текстом {text}")
    def send_text_to_field(self, element, text):
        self.browser.find_element(element.search_method, element.locator).send_keys(text)

    def fill_value_positive(self):
        self.wait_element_visible(AGE_FIELD, 2)
        self.send_text_to_field(AGE_FIELD, TestData.POS_AGE)
        self.send_text_to_field(HEIGHT, TestData.POS_HEIGHT)
        self.send_text_to_field(WEIGHT, TestData.POS_WEIGHT)

        self.click_element(GENDER)
        self.click_element(TYPE)
        self.click_element(VOLUME_ACTION)
        self.wait_element_clickable(SUBMIT, 2)
        self.click_element(SUBMIT)

    def fill_value_negative(self):
        self.wait_element_visible(AGE_FIELD, 2)
        self.send_text_to_field(AGE_FIELD, TestData.POS_AGE)
        self.send_text_to_field(HEIGHT, TestData.POS_HEIGHT)
        self.send_text_to_field(WEIGHT, TestData.NEGATIVE_WEIGHT)

        self.click_element(GENDER)
        self.click_element(TYPE)
        self.click_element(VOLUME_ACTION)
        self.wait_element_clickable(SUBMIT, 2)
        self.click_element(SUBMIT)

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

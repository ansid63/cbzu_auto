from selenium.common.exceptions import NoSuchElementException
import allure
from .pages.main_page import MainPage
import time


class TestCbzu:
    @allure.title("Позитивный тест расчёта КБЖУ")
    def test_positive_value(self, browser):
        new_user = MainPage(browser)
        new_user.open()

        # input info about user
        new_user.fill_value_positive()
        time.sleep(5)

        # check field
        new_user.check_numbers()


    @allure.title("Негативный тест расчёта КБЖУ")
    def test_negative_value(self, browser):
        new_user = MainPage(browser)
        new_user.open()

        # input info about user
        new_user.fill_value_negative()
        time.sleep(5)

        # check field
        try:
            new_user.check_numbers()
        except NoSuchElementException:
            print('Негативные данные не прошли')
        finally:
            print('Корректный негативный тест')

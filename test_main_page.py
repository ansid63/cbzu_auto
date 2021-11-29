from selenium.common.exceptions import NoSuchElementException

from .pages.main_page import MainPage
import time


def test_positive_value(browser):
    # link = "http://musclegain.ru/calculator_bzu.html"
    new_user = MainPage(browser)
    new_user.open()

    #input info about user
    new_user.fill_value_positive()
    time.sleep(5)

    # check field
    new_user.check_numbers()

def test_negative_value(browser):
    # link = "http://musclegain.ru/calculator_bzu.html"
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

    finally: print('Корректный негативный тест')





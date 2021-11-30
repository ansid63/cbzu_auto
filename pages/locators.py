from selenium.webdriver.common.by import By
import enum


class NamedElement(enum.Enum):
    def __init__(self, search_method, locator, locator_name):
        self.search_method = search_method
        self.locator = locator
        self.locator_name = locator_name

    AGE = (By.NAME, "ago", "Поле ввода 'Возраст'")
    HEIGHT = (By.NAME, "rost", "Поле ввода 'Рост'")
    WEIGHT = (By.NAME, "massa", "Поле ввода 'Вес'")
    GENDER = (By.XPATH, "//input[@name='pol' and @value='2']", "Поле выбора пола 'Мужской'")
    TYPE = (By.XPATH, "//input[@name='cel' and @value='1']", "Цель Снижение веса")
    VOLUME_ACTION = (By.XPATH, "//input[@name='obr' and @value='3']", "Поле выбора 'Активность Средняя'")
    SUBMIT = (By.CSS_SELECTOR, ".btn", "Кнопка Подтвердить")
    NUMBER_CHARIS_BENEDIKT = (By.XPATH, "//table[@id='res']/tbody/tr[2]/td[2]/b", "Число ЧБ")
    NUMBER_BAZAL_META = (By.XPATH, "//table[@id='res']/tbody/tr[3]/td[2]/b", "Число базального метаболизма")

from selenium.webdriver.common.by import By


class ElementWithName:
    def __init__(self, search_method, locator, locator_name):
        self.search_method = search_method
        self.locator = locator
        self.locator_name = locator_name

    def __str__(self):
        return self.locator_name

    def __repr__(self):
        return self.locator_name


AGE_FIELD = ElementWithName(By.NAME, "ago", "Поле ввода 'Возраст'")
HEIGHT = ElementWithName(By.NAME, "rost", "Поле ввода 'Рост'")
WEIGHT = ElementWithName(By.NAME, "massa", "Поле ввода 'Вес'")
GENDER = ElementWithName(By.XPATH, "//input[@name='pol' and @value='2']", "Поле выбора пола 'Мужской'")
TYPE = ElementWithName(By.XPATH, "//input[@name='cel' and @value='1']", "Цель Снижение веса")
VOLUME_ACTION = ElementWithName(By.XPATH, "//input[@name='obr' and @value='3']", "Поле выбора 'Активность Средняя'")
SUBMIT = ElementWithName(By.CSS_SELECTOR, ".btn", "Кнопка Подтвердить")
NUMBER_CHARIS_BENEDIKT = ElementWithName(By.XPATH, "//table[@id='res']/tbody/tr[2]/td[2]/b", "Число ЧБ")
NUMBER_BAZAL_META = ElementWithName(By.XPATH, "//table[@id='res']/tbody/tr[3]/td[2]/b", "Число базального метаболизма")

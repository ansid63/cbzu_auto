from selenium.webdriver.common.by import By


class BasePageLocators():
    #locators for value
    AGE = (By.NAME, "ago")
    HEIGHT = (By.NAME, "rost")
    WEIGHT = (By.NAME, "massa")
    GENDER = (By.XPATH, "//input[@name='pol' and @value='2']")
    TYPE = (By.XPATH, "//input[@name='cel' and @value='1']")
    VOLUME_ACTION = (By.XPATH, "//input[@name='obr' and @value='3']")
    SUBMIT = (By.CSS_SELECTOR, ".btn")

    #check fields
    NUMBER_CHARIS_BENEDIKT = (By.XPATH, "//table[@id='res']/tbody/tr[2]/td[2]/b")
    NUMBER_BAZAL_META = (By.XPATH, "//table[@id='res']/tbody/tr[3]/td[2]/b")


    #value for positive test
    POS_AGE = "37"
    POS_HEIGHT = "185"
    POS_WEIGHT = "80"
    NEGATIVE_WEIGHT = "-80"








from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class Element:

    def __init__(self, driver, **locator):

        self.driver = driver

        self.locator_key = list(locator.keys())[0]
        self.locator_value = locator[self.locator_key]
        self.locator = (eval('by.' + self.locator_key), self.locator_value)

    def element(self):

        wait(self.driver,10).until(EC.visibility_of_element_located(self.locator))
        return self.driver.find_element(*self.locator)

class Button(Element):

    def __init__(self, driver, wait_for=None, **locators):

        super().__init__(driver, **locators)

        self.wait_locator = None
        if wait_for is not None: self.wait_locator = (by.XPATH, wait_for)

    def click(self):

        print(self.locator)
        wait(self.driver,10).until(EC.element_to_be_clickable(self.locator))
        self.element().click()
        if self.wait_locator: wait(self.driver,10).until(EC.visibility_of_element_located(self.wait_locator))



class Field(Element):

    def click(self): self.element().click()
    def input(self, keys): self.element().send_keys(keys)
    def clear(self): self.element().clear()



import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from Pages.Base import TestAppium

class Search(TestAppium):
    def test_search_product(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        sh2_locator = (AppiumBy.ID, 'com.portonics.aarong:id/searchFragment')
        wait = WebDriverWait(self.driver, 10)
        sh2_field = wait.until(ec.element_to_be_clickable(sh2_locator))
        sh2_field.click()
        as1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/etSearch')
        as1 = "Kurta"
        wait = WebDriverWait(self.driver, 10)
        as1_field = wait.until(ec.presence_of_element_located(as1_locator))
        as1_field.send_keys(as1)
        assert as1_field.send_keys, "Failed to search"


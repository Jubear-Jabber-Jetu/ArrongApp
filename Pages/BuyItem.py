import unittest
from lib2to3.pgen2 import driver
from telnetlib import EC
from tkinter.tix import Select

import wait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Base import TestAppium

class Buy(TestAppium):
    def test_verify_checkout_cart(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        bl1_locator = (AppiumBy.ID, '//android.widget.FrameLayout[@content-desc="Cart"]')
        wait = WebDriverWait(self.driver, 10)
        bl1_field = wait.until(ec.element_to_be_clickable(bl1_locator))
        bl1_field.click()
        bl2_locator = (AppiumBy.ID, 'com.portonics.aarong:id/tvCheckOut')
        wait = WebDriverWait(self.driver, 10)
        bl2_field = wait.until(ec.element_to_be_clickable(bl2_locator))
        bl2_field.click()
        bl3_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnGuest')
        wait = WebDriverWait(self.driver, 10)
        bl3_field = wait.until(ec.element_to_be_clickable(bl3_locator))
        bl3_field.click()
        email_locator = (AppiumBy.ID, 'com.portonics.aarong:id/textinput_placeholder')
        email = "jubearjabberjetu@gmail.com"
        email_field = wait.until(ec.presence_of_element_located(email_locator))
        email_field.send_keys(email)
        fname_locator = (AppiumBy.ID, 'com.portonics.aarong:id/textinput_placeholder')
        fname = "Jubear"
        fname_field = wait.until(ec.presence_of_element_located(fname_locator))
        fname_field.send_keys(fname)
        lname_locator = (AppiumBy.ID, 'com.portonics.aarong:id/textLastName')
        lname = "Jabber"
        lname_field = wait.until(ec.presence_of_element_located(lname_locator))
        lname_field.send_keys(lname)
        mb_locator = (AppiumBy.ID, 'com.portonics.aarong:id/textMobileNumber')
        mb = "01684300844"
        mb_field = wait.until(ec.presence_of_element_located(mb_locator))
        mb_field.send_keys(mb)
        ad_locator = (AppiumBy.ID, 'com.portonics.aarong:id/textAddressOne')
        ad = "56, Kutubkhali, Jatrabari, Dhaka"
        ad_field = wait.until(ec.presence_of_element_located(ad_locator))
        ad_field.send_keys(ad)
        s8_locator = (AppiumBy.XPATH, '(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]')
        wait = WebDriverWait(self.driver, 10)
        s8_field = wait.until(ec.element_to_be_clickable(s8_locator))
        s8_field.click()


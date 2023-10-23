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
    def test_verify_my_account_is_available (self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        sh1_locator = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="My Account"]/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        b1_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]')
        wait = WebDriverWait(self.driver, 10)
        b1_field = wait.until(ec.element_to_be_clickable(b1_locator))
        assert b1_field.is_displayed(), "My Account option is not available."

    def test_verify_rewards_and_offer_is_available(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        sh1_locator = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="My Account"]/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        b2_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        b2_field = wait.until(ec.element_to_be_clickable(b2_locator))
        assert b2_field.is_displayed(), "Rewards and Offer option is not available."

    def test_verify_my_orders_is_available(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        sh1_locator = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="My Account"]/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        b2_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]')
        wait = WebDriverWait(self.driver, 10)
        b2_field = wait.until(ec.element_to_be_clickable(b2_locator))
        assert b2_field.is_displayed(), "My orders is not available."

    def test_verify_my_orders_is_available(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        sh1_locator = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="My Account"]/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        sh1_field.click()
        b2_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[3]')
        wait = WebDriverWait(self.driver, 10)
        b2_field = wait.until(ec.element_to_be_clickable(b2_locator))
        assert b2_field.is_displayed(), "Wishlist option is not available."
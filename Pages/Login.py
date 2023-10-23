import unittest
from telnetlib import EC
from tkinter.tix import Select

import wait as wait
from selenium.common import NoSuchElementException
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Base import TestAppium

class Login(TestAppium):


    def test_verify_log_button(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()

        try:
            el = (AppiumBy.ID, 'com.portonics.aarong:id/btnLoginNow')
            wait = WebDriverWait(self.driver, 10)
            el_field = wait.until(ec.element_to_be_clickable(el))
            el_field.click()
            print("Login button click verified")
            assert True, "Login button click was successful."
        except NoSuchElementException:
            print("Login button click failed")
            assert False, "Login button click failed: Element not found."


    def test_verify_log_in(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        el = (AppiumBy.ID, 'com.portonics.aarong:id/btnLoginNow')
        wait = WebDriverWait(self.driver, 10)
        el_field = wait.until(ec.element_to_be_clickable(el))
        el_field.click()
        try:
            wait = WebDriverWait(self.driver, 300)
            phone_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView')
            phone = "01684300844"
            phone_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(phone_locator))
            phone_field.send_keys(phone)
            #assert phone_field.get_attribute("text") == phone, f"Expected phone number {phone}, but found {phone_field.get_attribute('text')}"

            continue_button_locator = (AppiumBy.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[1]')
            continue_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(continue_button_locator))
            continue_button.click()
            assert True, "Login button click was successful."
            #login_check_loctor= (AppiumBy.XPATH, 'com.portonics.aarong:id/tvOtpHeading')
        except NoSuchElementException:
            print("Login button click failed")
            assert False, "Login button click failed: Element not found."
    def test_invalid_login(self) -> None:

            self.test_verify_log_button()
            phone_locator = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
            phone = "01908857338"
            phone_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(phone_locator))

            phone_field.clear()
            phone_field.send_keys(phone)

            # Assert that the phone number has been entered correctly
            assert phone_field.get_attribute(
                "text") == phone, f"Expected phone number {phone}, but found {phone_field.get_attribute('text')}"

            # Perform the continue button click
            continue_button_locator = (AppiumBy.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[1]')
            continue_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(continue_button_locator))
            continue_button.click()

            # Assert that an invalid login message is displayed
            invalid_login_message_locator = (AppiumBy.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView')
            invalid_login_message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(invalid_login_message_locator))
            assert "Invalid login" in invalid_login_message.text, "Invalid login message not displayed"


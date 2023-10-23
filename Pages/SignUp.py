import unittest
from tkinter.tix import Select

from selenium.common import NoSuchElementException
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Base import TestAppium

class SignUp(TestAppium):
    from selenium.common.exceptions import NoSuchElementException

    def test_verify_sign_up_button(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()

        try:
            wait = WebDriverWait(self.driver, 100)
            el = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[2]')

            el.click()
            print("Sign Up button click verified")
        except NoSuchElementException:
            print("Sign Up button not found")
            assert False
        else:
            assert True

    def test_verify_sign_up2(self) -> None:
        self.test_verify_sign_up_button()
        wait = WebDriverWait(self.driver, 300)
        first_name_locator = (AppiumBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
        last_name_locator = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')
        mobile_locator = (AppiumBy.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText')
        gender_dropdown_locator = (AppiumBy.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.Spinner')
        username = "Jubear"
        lastname = "Jabber"
        mobile = "01684300844"
        selected_gender = "Male"
        first_name_field = wait.until(ec.presence_of_element_located(first_name_locator))
        last_name_field = wait.until(ec.presence_of_element_located(last_name_locator))
        mobile_field = wait.until(ec.presence_of_element_located(mobile_locator))
        gender_dropdown = wait.until(ec.presence_of_element_located(gender_dropdown_locator))
        first_name_field.send_keys(username)
        last_name_field.send_keys(lastname)
        mobile_field.send_keys(mobile)
        gender_dropdown.click()
        gender_option_locator = (AppiumBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
        gender_option = wait.until(ec.presence_of_element_located(gender_option_locator))
        gender_option = wait.until(ec.presence_of_element_located(gender_option_locator))
        gender_option.click()
        try:
            wait = WebDriverWait(self.driver, 100)
            submit_button_locator = (AppiumBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
            submit_button = wait.until(ec.presence_of_element_located(submit_button_locator))
            submit_button.click()
            print("Continue button click verified")
            email_locator = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
            email = "jubearjabberjetu@gmail.com"
            email_field = wait.until(ec.presence_of_element_located(email_locator))
            email_field.send_keys(email)
            dob_locator = (AppiumBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')
            dob_button = wait.until(ec.presence_of_element_located(dob_locator))
            dob_button.click()
            edb_locator = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Switch to text input mode"]')
            edb_button = wait.until(ec.presence_of_element_located(edb_locator))
            edb_button.click()
            edb2_locator = (AppiumBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')
            edb2 = "08/27/98"
            edb2_field = wait.until(ec.presence_of_element_located(edb2_locator))
            edb2_field.send_keys(edb2)
            edb_button.click()
            pas3_locator = (AppiumBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]')
            pas3_button = wait.until(ec.presence_of_element_located(pas3_locator))
            pas3_button.click()

            pas_locator = (AppiumBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText')
            pas = "Jubear@#78"
            pas_field = wait.until(ec.presence_of_element_located(pas_locator))
            # After sending keys to the password field
            pas_field.send_keys(pas)
            pas2_locator = (AppiumBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.EditText')
            pas2 = "Jubear@#78"
            pas2_field = wait.until(ec.presence_of_element_located(pas2_locator))
            pas2_field.send_keys(pas2)
            cb_locator = (AppiumBy.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.CheckBox')
            cb_button = wait.until(ec.presence_of_element_located(cb_locator))
            cb_button.click()
            try:
                wait = WebDriverWait(self.driver, 100)
                submit_button_locator2 = (AppiumBy.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
                submit_button2 = wait.until(ec.presence_of_element_located(submit_button_locator2))
                submit_button2.click()
                print("Submit button click verified")
            except NoSuchElementException:
                print("Submit button not found")
                assert False
            else:
                assert True
        except NoSuchElementException:
            print("Continue button not found")
            assert False
        else:
            assert True






import unittest
from lib2to3.pgen2 import driver
from telnetlib import EC
from tkinter.tix import Select

import wait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Base import TestAppium

class AddToBag(TestAppium):
    def test_verify_add_to_bag(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        s1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        s1_field = wait.until(ec.element_to_be_clickable(s1_locator))
        assert s1_field is not None, "Start Shopping is not clickable"
        s1_field.click()
        print("Start Shopping is clickable")

        s2_locator = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Menu"]')
        wait = WebDriverWait(self.driver, 10)
        s2_field = wait.until(ec.element_to_be_clickable(s2_locator))
        assert s2_field is not None, "Menu is not clickable"
        s2_field.click()
        print("Menu is clickable")

        s3_locator = (AppiumBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
        wait = WebDriverWait(self.driver, 10)
        s3_field = wait.until(ec.element_to_be_clickable(s3_locator))
        assert s3_field is not None, "Men is not clickable"
        s3_field.click()
        print("Men is clickable")

        s4_locator = (AppiumBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
        wait = WebDriverWait(self.driver, 10)
        s4_field = wait.until(ec.element_to_be_clickable(s4_locator))
        assert s4_field is not None, "NEW ARRIVALS is not clickable"
        s4_field.click()
        print("NEW ARRIVALS is clickable")

        s5_locator = (AppiumBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]')
        wait = WebDriverWait(self.driver, 10)
        s5_field = wait.until(ec.element_to_be_clickable(s5_locator))
        assert s5_field is not None, "Item is not clickable"
        s5_field.click()
        print("Item is clickable")

        s6_locator = (AppiumBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.Button')
        wait = WebDriverWait(self.driver, 10)
        s6_field = wait.until(ec.element_to_be_clickable(s6_locator))
        assert s6_field is not None, "ADD TO BAG is not clickable"
        s6_field.click()
        print("ADD TO BAG is clickable")

        s8_locator = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show dropdown menu"]')
        wait = WebDriverWait(self.driver, 10)
        s8_field = wait.until(ec.element_to_be_clickable(s8_locator))
        assert s8_field is not None, "Select size is not clickable"
        s8_field.click()
        print("Select size is clickable")

        element_with_m_locator = (MobileBy.XPATH, "//*[contains(@text, 'M')]")
        wait = WebDriverWait(self.driver, 10)

        try:
            element_with_m = wait.until(EC.element_to_be_clickable(element_with_m_locator))
            element_with_m.click()
            print("Element with 'M' is clickable")

            s7_locator = (AppiumBy.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android/widget.FrameLayout/android/widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.Button')
            wait = WebDriverWait(self.driver, 10)
            s7_field = wait.until(ec.element_to_be_clickable(s7_locator))
            assert s7_field is not None, "Quantity is not clickable"
            s7_field.click()
            print("Quantity is clickable")

            s11_locator = (AppiumBy.XPATH, '')  # Add your XPath for s11
            wait = WebDriverWait(self.driver, 10)
            s11_field = wait.until(ec.element_to_be_clickable(s11_locator))
            assert s11_field is not None, "Done is not clickable"
            s11_field.click()
            print("Done is clickable")
        except Exception as e:
            print("Element with 'M' not found or not clickable:", e)

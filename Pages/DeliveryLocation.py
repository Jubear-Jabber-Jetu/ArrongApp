from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from Pages.Base import TestAppium

class Delivery(TestAppium):
    def test_verify_set_country(self) -> None:
        self.swipe_left()
        b1_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Spinner')
        wait = WebDriverWait(self.driver, 10)
        b1_field = wait.until(ec.element_to_be_clickable(b1_locator))

        # Use assert to verify that the element is clickable
        assert b1_field.is_enabled(), "Element is not clickable"
        b1_field.click()
        b2_locator = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]')
        wait = WebDriverWait(self.driver, 10)
        b2_field = wait.until(ec.element_to_be_clickable(b2_locator))

        # Use assert to verify that the element is clickable
        assert b2_field.is_enabled(), "Element is not clickable"
        b2_field.click()
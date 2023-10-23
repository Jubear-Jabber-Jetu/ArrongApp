from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Base import TestAppium

class Shopping(TestAppium):
    def test_verify_start_shopping(self) -> None:
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()

        sh1_locator = (AppiumBy.ID, 'com.portonics.aarong:id/btnStartShopping')
        wait = WebDriverWait(self.driver, 10)
        sh1_field = wait.until(ec.element_to_be_clickable(sh1_locator))
        assert sh1_field, "Start Shopping button is not clickable."
        sh1_field.click()

        menu_locator = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Menu"]')
        menu_frame = wait.until(ec.element_to_be_clickable(menu_locator))
        assert menu_frame, "Menu frame is not clickable."
        menu_frame.click()

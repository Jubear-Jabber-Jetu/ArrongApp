import unittest


from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel XL',
    appPackage='com.portonics.aarong',
    appActivity='com.ranosys.aarong.ui.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723/wd/hub'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def swipe_left(self):
        # Define the screen dimensions
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        # Perform a swipe gesture to the left
        start_x = width * 0.8
        end_x = width * 0.2
        y = height * 0.5
        duration = 800  # Adjust the duration as needed
        self.driver.swipe(start_x, y, end_x, y, duration)





if __name__ == '__main__':
    unittest.main()
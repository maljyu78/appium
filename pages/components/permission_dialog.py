from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class PermissionDialog (BasePage):

    def __init__(self, driver):
            super().__init__(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "permission_message": (AppiumBy.ID, "com.android.permissioncontroller:id/permission_message"),
                "google_message": (AppiumBy.ID, "com.google.android.gms:id/message"),
                "alert_message": (AppiumBy.ID, "android:id/alertTitle"),
                "agree_button": (AppiumBy.ID, "android:id/button1"),
                "degree_button": (AppiumBy.ID, "android:id/button2"),
                "while_using_app": (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
                "only_this_time": (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button"),
                "dont_allow": (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button"),
            }

        elif self.platform == "ios":
            locators = {
                "container": (AppiumBy.ACCESSIBILITY_ID, "container header"),
                "textview": (AppiumBy.CLASS_NAME, "android.widget.TextView"),

            }
        return locators[name]

    # Action
    def is_message_displayed(self, locator_name, timeout=5):
        locator = self._get_locator(locator_name)

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True

        except TimeoutException:
            return False
    
    def get_permission_message_status(self):
        return self.is_message_displayed("permission_message")

    def allow_only_this_time(self):
        locator = self._get_locator("only_this_time")

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def get_google_message_status(self):
        return self.is_message_displayed("google_message")

    def click_agree_button(self):
        locator = self._get_locator("agree_button")

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_alert_message_status(self):
        return self.is_message_displayed("alert_message")
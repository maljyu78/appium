from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.components.header import Header
from pages.components.header import SortButton
from pages.components.header import SideMenuButton
from pages.components.permission_dialog import PermissionDialog

class AppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.sort = SortButton(driver)
        self.side = SideMenuButton(driver)
        self.permission = PermissionDialog(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "container": (AppiumBy.ACCESSIBILITY_ID, "container header"),
                "textview": (AppiumBy.CLASS_NAME, "android.widget.TextView"),
                "button_agree": (AppiumBy.ID, "android:id/button1"),
                "button_cancel": (AppiumBy.ID, "android:id/button2")
            }

        elif self.platform == "ios":
            locators = {
                "container": (AppiumBy.ACCESSIBILITY_ID, "container header"),
                "textview": (AppiumBy.CLASS_NAME, "android.widget.TextView"),

            }
        return locators[name]

    # Action

    def get_title_name(self):
        container = self.wait.until(
            EC.visibility_of_element_located(
                self._get_locator("container")
            )
        )

        title_name = container.find_element(
            *self._get_locator("textview")
        )

        return title_name.text

    def permission_message_is_displayed(self):
        return self.permission.get_permission_message_status()

    def click_only_this_time(self):
        self.permission.allow_only_this_time()

    def google_message_is_displayed(self):
        return self.permission.get_google_message_status()

    def alert_message_is_displayed(self):
        return self.permission.get_alert_message_status()

    def click_agree_button(self):
        self.permission.click_agree_button()
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.components.header import Header
from pages.components.header import SortButton
from pages.components.header import SideMenuButton

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.sort = SortButton(driver)
        self.side = SideMenuButton(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "container": (AppiumBy.ACCESSIBILITY_ID, "container header"),
                "textview": (AppiumBy.CLASS_NAME, "android.widget.TextView"),
                "username_input_filed": (AppiumBy.ACCESSIBILITY_ID, "Username input field"),
                "password_input_filed": (AppiumBy.ACCESSIBILITY_ID, "Password input field"),
                "login_button": (AppiumBy.ACCESSIBILITY_ID, "Login button"),
            }

        elif self.platform == "ios":
            locators = {
                "container": (AppiumBy.ACCESSIBILITY_ID, "Products"),
                "textview": (AppiumBy.CLASS_NAME, "android.widget.TextView"),
            }
        return locators[name]

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

    def input_username(self, username):
        self.find_element(
            self._get_locator("username_input_filed")
        ).send_keys(username)

    def input_password(self, password):
        self.find_element(
            self._get_locator("password_input_filed")
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self._get_locator("login_button")
            )
        ).click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "sort_button": (AppiumBy.ACCESSIBILITY_ID, "sort button"),
                "cart_badge": (AppiumBy.ACCESSIBILITY_ID, "cart badge"),
                "menu_button": (AppiumBy.ACCESSIBILITY_ID, "open menu"),
            }

        return locators[name]

    def _get_locator(self, name):
            if self.platform == "ios":
                locators = {
                "sort_button": (AppiumBy.ACCESSIBILITY_ID, "sort button"),
                "cart_badge": (AppiumBy.ACCESSIBILITY_ID, "cart badge"),
                "menu_button": (AppiumBy.ACCESSIBILITY_ID, "open menu"),
                }
    
            return locators[name]

    # Action
    def click_sort_button(self):
        self.click(self._get_locator("sort_button"))

    def click_cart_badge(self):
        self.click(self._get_locator("cart_badge"))

    def click_side_menu(self):
        self.click(self._get_locator("menu_button"))

class SortButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "sort_button": (AppiumBy.ACCESSIBILITY_ID, "sort button"),
                "name_asc": (AppiumBy.ACCESSIBILITY_ID, "nameAsc"),
                "name_desc": (AppiumBy.ACCESSIBILITY_ID, "nameDesc"),
                "price_asc": (AppiumBy.ACCESSIBILITY_ID, "priceAsc"),
                "price_desc": (AppiumBy.ACCESSIBILITY_ID, "priceDesc"),
            }

        return locators[name]

    def _get_locator(self, name):
            if self.platform == "ios":
                locators = {
                "sort_button": (AppiumBy.ACCESSIBILITY_ID, "sort button"),
                "name_asc": (AppiumBy.ACCESSIBILITY_ID, "nameAsc"),
                "name_desc": (AppiumBy.ACCESSIBILITY_ID, "nameDesc"),
                "price_asc": (AppiumBy.ACCESSIBILITY_ID, "priceAsc"),
                "price_desc": (AppiumBy.ACCESSIBILITY_ID, "priceDesc"),
                }
    
            return locators[name]

    # Action
    def click_name_asc(self):
        self.click(self._get_locator("name_asc"))

    def click_name_desc(self):
        self.click(self._get_locator("name_desc"))

    def click_price_asc(self):
        self.click(self._get_locator("price_asc"))

    def click_price_desc(self):
        self.click(self._get_locator("price_desc"))

class SideMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "menu_catalog": (AppiumBy.ACCESSIBILITY_ID, "menu item catalog"),
                "menu_webview": (AppiumBy.ACCESSIBILITY_ID, "menu item webview"),
                "menu_qr_scan": (AppiumBy.ACCESSIBILITY_ID, "menu item qr code scanner"),
                "menu_geo_location": (AppiumBy.ACCESSIBILITY_ID, "menu item geo location"),
                "menu_drawing": (AppiumBy.ACCESSIBILITY_ID, "menu item drawing"),
                "menu_about": (AppiumBy.ACCESSIBILITY_ID, "menu item about"),
                "menu_reset_app_state": (AppiumBy.ACCESSIBILITY_ID, "menu item reset app"),
                "menu_finger_print": (AppiumBy.ACCESSIBILITY_ID, "menu item biometrics"),
                "menu_login": (AppiumBy.ACCESSIBILITY_ID, "menu item log in"),
                "menu_logout": (AppiumBy.ACCESSIBILITY_ID, "menu item log out"),
                "menu_api_calls": (AppiumBy.ACCESSIBILITY_ID, "menu item api calls"),
                "menu_sauce_bot_video": (AppiumBy.ACCESSIBILITY_ID, "menu item sauce bot video"),
            }

        return locators[name]

    def _get_locator(self, name):
            if self.platform == "ios":
                locators = {
                "menu_catalog": (AppiumBy.ACCESSIBILITY_ID, "menu item catalog"),
                "menu_webview": (AppiumBy.ACCESSIBILITY_ID, "menu item webview"),
                "menu_qr_scan": (AppiumBy.ACCESSIBILITY_ID, "menu item qr code scanner"),
                "menu_geo_location": (AppiumBy.ACCESSIBILITY_ID, "menu item geo location"),
                "menu_drawing": (AppiumBy.ACCESSIBILITY_ID, "menu item drawing"),
                "menu_about": (AppiumBy.ACCESSIBILITY_ID, "menu item about"),
                "menu_reset_app_state": (AppiumBy.ACCESSIBILITY_ID, "menu item reset app"),
                "menu_finger_print": (AppiumBy.ACCESSIBILITY_ID, "menu item biometrics"),
                "menu_login": (AppiumBy.ACCESSIBILITY_ID, "menu item log in"),
                "menu_logout": (AppiumBy.ACCESSIBILITY_ID, "menu item log out"),
                "menu_api_calls": (AppiumBy.ACCESSIBILITY_ID, "menu item api calls"),
                "menu_sauce_bot_video": (AppiumBy.ACCESSIBILITY_ID, "menu item sauce bot video"),
                }

            return locators[name]

    # Action
    def click_catalog(self):
        self.click(self._get_locator("menu_catalog"))

    def click_webview(self):
            self.click(self._get_locator("menu_webview"))

    def click_qr_scan(self):
            self.click(self._get_locator("menu_qr_scan"))

    def click_geo_location(self):
            self.click(self._get_locator("menu_geo_location"))

    def click_drawing(self):
            self.click(self._get_locator("menu_drawing"))

    def click_about(self):
            self.click(self._get_locator("menu_about"))

    def click_reset(self):
        self.click(self._get_locator("menu_reset_app_status"))

    def click_finger_print(self):
            self.click(self._get_locator("menu_finger_print"))

    def click_login(self):
            self.click(self._get_locator("menu_login"))

    def click_logout(self):
            self.click(self._get_locator("menu_logout"))

    def click_api_calls(self):
            self.click(self._get_locator("menu_api_calls"))

    def click_sauce_bot_video(self):
            self.click(self._get_locator("menu_sauce_bot_video"))
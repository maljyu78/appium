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
        elif self.platform == "ios":
            locators = {
                "sort_button": (AppiumBy.ACCESSIBILITY_ID, "sort button"),
                "cart_badge": (AppiumBy.ACCESSIBILITY_ID, "cart badge"),
                "menu_button": (AppiumBy.ACCESSIBILITY_ID, "open menu"),
            }

        return locators[name]

    # Action
    def click_sort_button(self):
        sort_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self._get_locator("sort_button")
            )
        )
        sort_btn.click()

    def click_cart_badge(self):
        cart_badge = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self._get_locator("cart_badge")
            )
        )
        cart_badge.click()

    def click_side_menu(self):
        side_menu_button = self.wait.until(
            EC.element_to_be_clickable(
                self._get_locator("menu_button")
            )
        )
        side_menu_button.click()

    def get_cart_count(self):
        badge = self.wait.until(
            EC.presence_of_element_located(
                self._get_locator("cart_badge")
            )
        )
        if self.platform == "android":
            cart_count = badge.find_elements(
                AppiumBy.CLASS_NAME,
                "android.widget.TextView"
            )

        elif self.platform == "ios":
            cart_count = badge.find_elements(
                AppiumBy.CLASS_NAME,
                "XCUIElementTypeStaticText"
            )

        else:
            raise NotImplementedError(
                f"Unsupported platform: {self.platform}"
            )
        
        return len(cart_count) > 0
        
class SortButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "name_asc": (AppiumBy.ACCESSIBILITY_ID, "nameAsc"),
                "name_desc": (AppiumBy.ACCESSIBILITY_ID, "nameDesc"),
                "price_asc": (AppiumBy.ACCESSIBILITY_ID, "priceAsc"),
                "price_desc": (AppiumBy.ACCESSIBILITY_ID, "priceDesc"),
            }

        elif self.platform == "ios":
            locators = {
                "name_asc": (AppiumBy.ACCESSIBILITY_ID, "nameAsc"),
                "name_desc": (AppiumBy.ACCESSIBILITY_ID, "nameDesc"),
                "price_asc": (AppiumBy.ACCESSIBILITY_ID, "priceAsc"),
                "price_desc": (AppiumBy.ACCESSIBILITY_ID, "priceDesc"),
            }

        return locators[name]

    # Action
    def find_sort_button(self, button_name):
        element = self.find_element(self._get_locator(button_name))
        print(f"[DEBUG] {button_name}: {element is not None}")

        return element

    def click_name_asc(self):
        self.click(self._get_locator("name_asc"))

    def click_name_desc(self):
        self.click(self._get_locator("name_desc"))

    def click_price_asc(self):
        self.click(self._get_locator("price_asc"))

    def click_price_desc(self):
        self.click(self._get_locator("price_desc"))

class SideMenuButton(BasePage):
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

        elif self.platform == "ios":
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

    def find_side_buttons(self, button_name):
            element = self.find_element(self._get_locator(button_name))
            print(f"[DEBUG] {button_name}: {element is not None}")
    
            return element
    
    def click_menu(self, names):
        locator = self._get_locator(names)

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()
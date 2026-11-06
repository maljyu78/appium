from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BasePage
from selenium.common.exceptions import StaleElementReferenceException

class ProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "product_detail_name": (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("container header")'
                    '.childSelector(new UiSelector().className("android.widget.TextView"))'
                ),
                "product_detail_price": (AppiumBy.ACCESSIBILITY_ID, "product price"),
                "back_button": (AppiumBy.ACCESSIBILITY_ID, "Back"),
            }

        elif self.platform == "ios":
            locators = {
                "product_detail_name": (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("container header")'
                    '.childSelector(new UiSelector().className("android.widget.TextView"))'
                ),
                "product_detail_price": (AppiumBy.ACCESSIBILITY_ID, "product price"),
                "back_button": (AppiumBy.ACCESSIBILITY_ID, "Back"),
            }
        return locators[name]

    def get_detail_info(self):
        name = self.find_element(
            self._get_locator("product_detail_name")
        )

        price = self.find_element(
            self._get_locator("product_detail_price")
        )

        return {
            "name": name.text.strip(),
            "price": price.text.strip()
        }
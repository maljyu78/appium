from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.platform = driver.platform.lower()
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.enter_text(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def hide_keyboard(self):
        try:
            if self.platform == "android" :
                self.driver.hide.keyboard()

            elif self.platform == "ios":
                self.click((AppiumBy.ACCESSOBILITY_ID, "Done"))

        except Exception as e:
            print('')

    def go_back(self):
        if self.platform == "android":
            self.driver.press_keycode(4)

        elif self.platform == "ios":
            self.click((AppiumBy.ACCESSIBILITY_ID, "Back"))

    def scroll_down(self) -> bool:

        if self.platform != "android":
            raise NotImplementedError(
                f"Scroll is not implemented for platform: {self.platform}"
            )

        screen_size = self.driver.get_window_size()

        width = screen_size["width"]
        height = screen_size["height"]

        return self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(width * 0.1),
                "top": int(height * 0.2),
                "width": int(width * 0.8),
                "height": int(height * 0.6),
                "direction": "down",
                "percent": 0.7,
            },
        )
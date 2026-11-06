from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.components.header import Header

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)

    # Locator
    def _get_locator(self, name):
        if self.platform == "android":
            locators = {
                "product_title": (AppiumBy.ACCESSIBILITY_ID, "container header"),
                "product_cards": (AppiumBy.ACCESSIBILITY_ID, "store item"),
                "product_names": (AppiumBy.ACCESSIBILITY_ID, "store item text"),
                "product_prices": (AppiumBy.ACCESSIBILITY_ID, "store item price"),
                "review_star1": (AppiumBy.ACCESSIBILITY_ID, "review star 1"),
                "review_star2": (AppiumBy.ACCESSIBILITY_ID, "review star 2"),
                "review_star3": (AppiumBy.ACCESSIBILITY_ID, "review star 3"),
                "review_star4": (AppiumBy.ACCESSIBILITY_ID, "review star 4"),
                "review_star5": (AppiumBy.ACCESSIBILITY_ID, "review star 5"),
                "close_modal_button": (AppiumBy.ACCESSIBILITY_ID, "Close Modal button"),
            }

        elif self.platform == "ios":
            locators = {
                "product_title": (AppiumBy.ACCESSIBILITY_ID, "Products"),
                "product_cards": (AppiumBy.ACCESSIBILITY_ID, "store item"),
                "product_names": (AppiumBy.ACCESSIBILITY_ID, "store item text"),
                "product_prices": (AppiumBy.ACCESSIBILITY_ID, "store item price"),
                "review_star1": (AppiumBy.ACCESSIBILITY_ID, "review star 1"),
                "review_star2": (AppiumBy.ACCESSIBILITY_ID, "review star 2"),
                "review_star3": (AppiumBy.ACCESSIBILITY_ID, "review star 3"),
                "review_star4": (AppiumBy.ACCESSIBILITY_ID, "review star 4"),
                "review_star5": (AppiumBy.ACCESSIBILITY_ID, "review star 5"),
                "close_modal_button": (AppiumBy.ACCESSIBILITY_ID, "Close Modal button"),
            }
        return locators[name]

    # Action
    def catalog_displayed(self):
        try:
            return self.find_element(
                self._get_locator("product_title")
                ).is_displayed()
        except Exception:
            return False

    def find_product_card(self, product_name):
        max_scrolls = 10
        scroll_count = 0

        while True:
            self.wait.until(
                EC.presence_of_all_elements_located(
                    self._get_locator("product_cards")
                )
            )

            cards = self.driver.find_elements(
                *self._get_locator("product_cards")
            )

            target_card = None

            for card in cards:
                name_elements = card.find_elements(
                    *self._get_locator("product_names")
                )

                if not name_elements:
                    continue

                name = name_elements[0].text.strip()

                if name == product_name:
                    target_card = card
                    break

            if target_card is not None:
                return target_card

            if scroll_count >= max_scrolls:
                raise NoSuchElementException(
                    f"Product not found after {max_scrolls} scrolls: "
                    f"{product_name}"
                )

            self.scroll_down()
            scroll_count += 1

    def get_product_info(self, card):
        names = card.find_elements(
            *self._get_locator("product_names")
        )
        prices = card.find_elements(
            *self._get_locator("product_prices")
        )

        return {
            "name": names[0].text.strip() if names else None,
            "price": prices[0].text.strip() if prices else None
        }

    def click_all_product(self, product_card):
        product_name = product_card.find_element(
            *self._get_locator("product_names")
        )
        product_name.click()

    def click_review_star(self, card, star_number):
        star = WebDriverWait(card, 10).until(
            EC.element_to_be_clickable(
                self._get_locator(f"review_star{star_number}")
            )
        )

        star.click()

    def check_modal_button(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self._get_locator("close_modal_button")
                )
            )
            return True

        except TimeoutException:
            return False

    def click_close_modal(self):
        self.click(self._get_locator("close_modal_button"))    

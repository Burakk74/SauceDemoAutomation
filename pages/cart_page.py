from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for SauceDemo Cart Page."""

    # locators
    CART_TITLE = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver=WebDriver):
        super().__init__(driver)
        self.url = "cart.html"

    def is_on_cart_page(self) -> bool:
        """Check if the current page is the cart page."""
        try:
            title_element = self.wait_for_element_to_be_visible(self.CART_TITLE, timeout=5)
            return self.find_element(self.CART_TITLE).text == "Your Cart"
        except TimeoutException:
            return False

    def go_to_checkout(self):
        """It continues to the checkout page."""
        self.wait_for_element_to_be_clickable(self.CHECKOUT_BUTTON).click()
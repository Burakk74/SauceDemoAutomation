from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    """Page Object for SauceDemo payment analysis (Checkout: Step 1, Step 2 and Completion)."""

    # locators (Payment step 1: Users info)
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    #Locators (Payment step 2: Overview)
    FINISH_BUTTON = (By.ID, "finish")

    # Locators (Payment step 3: Completion)
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")


    def __init__(self, driver=WebDriver):
        super().__init__(driver)
        self.url ="checkout-step-one.html"

    def fill_user_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill in user information on the checkout step 1 page."""
        self.input_text(self.FIRST_NAME_FIELD, first_name)
        self.input_text(self.LAST_NAME_FIELD, last_name)
        self.input_text(self.POSTAL_CODE_FIELD, postal_code)
        time.sleep(2)  # Short wait to ensure inputs are registered
        self.click_element(self.CONTINUE_BUTTON)


    def finalize_checkout(self):
        """Click the finish button to complete the checkout process."""
        self.wait_for_element_to_be_clickable(self.FINISH_BUTTON).click()



    def is_order_complete(self) -> bool:
        """Check if the order completion header is displayed."""
        try:
            #It checks for succesfull message header in comepletion page
            header_text = self.wait_for_element_to_be_clickable(self.COMPLETE_HEADER).text
            return "Thank you for your order!" in header_text
        except TimeoutException:
            return False
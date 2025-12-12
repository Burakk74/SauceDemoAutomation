import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME
from selenium.webdriver.remote.webdriver import WebDriver


#Successful login test
def test_successful_login(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    #It checks the is login success with valid values
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

     
    assert products_page.is_on_products_page(), "Products page did not load after successful login."
    print("Login successful, Products page loaded.")


#Unsuccessful login test
def test_unsuccessful_login(driver: WebDriver):
    login_page = LoginPage(driver)

    #It checks the is login fails with invalid values

    print("\n-> Step 1: Using invalid username to test unsuccessful login.")
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)

    assert login_page.get_error_message(), "Error message not displayed for invalid login."

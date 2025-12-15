import time
import pytest
from pages.products_page import ProductsPage
from selenium.webdriver.remote.webdriver import WebDriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


#Pytest use automatically the 'driver' fixture defined in 'conftest.py'
def test_add_first_item_to_cart(logged_in_driver: WebDriver):
    """A scenario for adding items to the cart and validating the cart counter in a logged-in session."""
    driver = logged_in_driver
    products_page = ProductsPage(driver)
    
 
    #Sure that we are on the products page
    assert products_page.is_on_products_page(), "The test did not start on theroducts page after successful login."


    #Step 1: Verify initial cart count is zero
    print("-> Step 1: Verifying the is cart empty on start of test.")
    initial_cart_count = products_page.get_cart_count()
    assert initial_cart_count == 0, f"Cart must be empty but {initial_cart_count} items were found."

    #Step 2: Add the first item to the cart
    print("-> Step 2: Adding the first item to the cart.")
    products_page.add_first_item_to_cart()

    #Step 3: Verify cart count is one
    print("-> Step 3: Verifying the cart count is 1 after adding an item.")
    final_cart_count = products_page.get_cart_count()

    assert final_cart_count == 1, f"Cart count should be 1 after adding an item, but found {final_cart_count}."

    print("Item successfully added to the cart, cart count is now 1.")

def test_complete_purchase_process(logged_in_driver: WebDriver) -> None: 
    """a scenario for completing a purchase process."""

    driver = logged_in_driver
    products_page = ProductsPage(driver)

    # 1. Add the first item to the cart

    products_page.add_first_item_to_cart()
    assert products_page.get_cart_count() == 1, "The item not added to cart."

    time.sleep(2)  # Short wait to ensure cart updates


    # 2. Go to the cart 
    products_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_on_cart_page(), "Not on the cart page."

    time.sleep(2)  # Short wait to ensure page loads


    # 3. Start the checkout process
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(driver) 
 


    # 4. Fill in user information
    checkout_page.fill_user_info("Test", "User", "34000")

    time.sleep(2)  # Short wait to ensure page loads


    # Complete the purchase
    checkout_page.finalize_checkout()

    # 6. Verify the order completion
    assert checkout_page.is_order_complete(), "The order was not completed successfully."

    print("\n Purchase process completed successfully .")
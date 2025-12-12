 
from .base_page import BasePage
from selenium.webdriver.common.by import By

 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time  

class ProductsPage(BasePage):
    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE_BUTTON_FOR_FIRST_ITEM = (By.XPATH, "(//button[text()='Remove'])[1]")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    # Pop-up butonu locator'ı
    GOOGLE_POPUP_TAMAM_BUTTON = (By.XPATH, "//button[text()='Tamam']")
    
     
    def close_google_security_popup(self):
        print("-> Pop-up kapatma metodu çağrıldı.")
        try:
            # Pop-up'ın görünmesini bekler
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.GOOGLE_POPUP_TAMAM_BUTTON)
            )
            
            # JavaScript ile zorla tıkla
            self.click_via_js(self.GOOGLE_POPUP_TAMAM_BUTTON)
            
            print("-> Güvenlik pop-up'ı (JS ile) kapatıldı.")
            time.sleep(1) # Kapanma için kısa bir bekleme
            
        except TimeoutException:
            print("-> Güvenlik pop-up'ı görünmedi, devam ediliyor.")
            pass

    def is_on_products_page(self):
        # ... (mevcut kod) ...
        try:
            return self.find_element(self.PRODUCTS_TITLE).text == "Products"
        except:
            return False

    def add_first_item_to_cart(self):
        # ... (mevcut kod) ...
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        # ... (mevcut kod) ...
        try:
            return int(self.find_element(self.SHOPPING_CART_BADGE).text)
        except:
            return 0
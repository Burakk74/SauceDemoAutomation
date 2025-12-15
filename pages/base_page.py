from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self,driver=WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self,locator: tuple):
        
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator: tuple, timeout=10):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
    def wait_for_element_to_be_clickable(self, locator: tuple, timeout=10):
            
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
    
    def click_element(self, locator: tuple, timeout=10):
            
            self.wait_for_element_to_be_clickable(locator, timeout).click()


    def input_text(self, locator: tuple, text: str, timeout=10):
             
            element = self.wait_for_element_to_be_visible(locator, timeout)
            element.clear() # Mevcut metni temizle (opsiyonel ama iyi bir pratik)
            element.send_keys(text)



# The method of checking element presence
    def is_element_present(self, locator: tuple) -> bool:
        
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    def click(self, locator: tuple):
        """It clicks on element."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: tuple, text: str):
        """It write text to element."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        """It returns the title of the current page."""
        return self.driver.title
    
 
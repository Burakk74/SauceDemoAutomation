from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, """//*[@id="login_button_container"]/div/form/div[3]/h3""") #Locatr for error message

    def login(self,username,password):
        """It enter username and password and click login button."""
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    def get_error_message(self):
        """It checks and returns error message text."""
        try:
            self.find_element(self.ERROR_MESSAGE)
            return True
        except:
            return False
        
    def is_error_message_displayed(self) -> bool:
        """It checks if the error message is displayed."""
        return self.is_element_present(self.ERROR_MESSAGE)
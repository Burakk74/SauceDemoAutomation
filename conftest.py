import pytest
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from typing import Iterator 
from utils.test_data import BASE_URL, VALID_USERNAME, VALID_PASSWORD 
from pages.login_page import LoginPage 
from pages.products_page import ProductsPage 

@pytest.fixture(scope="session")
def browser_options() -> Options:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")    
    options.add_argument("--enable-popup-blocking")
     
    
    return options

@pytest.fixture(scope="function")
def driver(browser_options: Options) -> Iterator[WebDriver]: 
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=browser_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    time.sleep(2)  
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver: WebDriver) -> Iterator[WebDriver]:
     
    login_page = LoginPage(driver)
         
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    yield driver
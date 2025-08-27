from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://www.saucedemo.com/"
    
    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("tomsmith")
sleep(2)
password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("SuperSecretPassword!")

blue_button = "button.radius"

click_button = driver.find_element(By.CSS_SELECTOR, blue_button)
click_button.click()
sleep(2)

flash_message = driver.find_element(By.CSS_SELECTOR, "#flash.success")

message_text = flash_message.text
print("Текст сообщения:", message_text)
driver.quit()

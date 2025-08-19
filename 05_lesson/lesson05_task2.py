from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")

# CSS-селектор для кнопки с несколькими классами
blue_button = "button.btn.btn-primary"

click_button = driver.find_element(By.CSS_SELECTOR, blue_button)
click_button.click()
click_button.click()
click_button.click()

sleep(5)
driver.quit()

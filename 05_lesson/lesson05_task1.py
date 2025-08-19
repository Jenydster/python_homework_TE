from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

# CSS-селектор для кнопки с несколькими классами
blue_button = ".btn.btn-primary"


def click_and_accept_alert():
    driver.find_element(By.CSS_SELECTOR, blue_button).click()
    sleep(0.5)  # небольшая пауза, чтобы успел появиться alert
    alert = driver.switch_to.alert
    alert.accept()


# 1-й клик
click_and_accept_alert()

# 2-й клик
click_and_accept_alert()

# 3-й клик
click_and_accept_alert()

sleep(5)
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
input_field = "input[type='text']"
search_input = driver.find_element(By.CSS_SELECTOR, input_field)
search_input.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(4)
name_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

txt = name_btn.text
print(txt)

driver.quit()

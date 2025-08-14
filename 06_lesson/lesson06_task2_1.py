from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Импортируем Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Создаем объект опций Chrome
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")  # Игнорировать ошибки сертификатов
chrome_options.add_argument("--ignore-ssl-errors")  # Игнорировать SSL ошибки
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options  # Передаем опции
)

driver.get("http://uitestingplayground.com/textinput")
input_field = "input[type='text']"
search_input = driver.find_element(By.CSS_SELECTOR, input_field)
search_input.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
wait = WebDriverWait(driver, 10)
name_btn = wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"),
        "SkyPro"
    )
)
name_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

txt = name_btn.text
print(txt)

driver.quit()

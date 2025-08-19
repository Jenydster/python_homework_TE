from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_delay_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        wait = WebDriverWait(driver, 60)

        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")


        def safe_click(text):
            btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']")))
            try:
                btn.click()
            except:
                driver.execute_script("arguments[0].click();", btn)

        safe_click("7")
        safe_click("+")
        safe_click("8")
        safe_click("=")


        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        print("Результат:", result_text)

        assert result_text == "15", f"Ожидался 15, получено {result_text}"

    finally:
        driver.quit()


test_delay_calculator()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def safe_click(self, text):
        """Кликаем по кнопке, используя JS, если обычный click не сработал"""
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']")))
        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

    def wait_for_result(self, expected_text):
        """Ждём, пока результат появится на экране"""
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), str(expected_text)))

    def get_result(self):
        return self.driver.find_element(By.CLASS_NAME, "screen").text

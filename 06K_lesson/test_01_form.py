from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    edge_driver_path = r"C:\Users\jenyd\OneDrive\Рабочий стол\Python_homework\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        input_fn = "input[name='first-name']"
        first_name_input = driver.find_element(By.CSS_SELECTOR, input_fn)
        first_name_input.send_keys("Иван")

        input_ln = "input[name='last-name']"
        last_name_input = driver.find_element(By.CSS_SELECTOR, input_ln)
        last_name_input.send_keys("Петров")

        input_address = "input[name='address']"
        adress_input = driver.find_element(By.CSS_SELECTOR, input_address)
        adress_input.send_keys("Ленина, 55-3")

        input_email = "input[name='e-mail']"
        p_email_input = driver.find_element(By.CSS_SELECTOR, input_email)
        p_email_input.send_keys("test@skypro.com")

        input_phone = "input[name='phone']"
        phone_input = driver.find_element(By.CSS_SELECTOR, input_phone)
        phone_input.send_keys("+7985899998787")

        input_zc = "input[name='zip-code']"
        zip_code_input = driver.find_element(By.CSS_SELECTOR, input_zc)
        zip_code_input.send_keys("")

        input_city = "input[name='city']"
        city_input = driver.find_element(By.CSS_SELECTOR, input_city)
        city_input.send_keys("Москва")

        input_country = "input[name='country']"
        country_input = driver.find_element(By.CSS_SELECTOR, input_country)
        country_input.send_keys("Россия")

        input_jp = "input[name='job-position']"
        job_input = driver.find_element(By.CSS_SELECTOR, input_jp)
        job_input.send_keys("QA")

        input_company = "input[name='company']"
        company_input = driver.find_element(By.CSS_SELECTOR, input_company)
        company_input.send_keys("SkyPro")

        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))

        # Проверки
        zip_code_field = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class"), "ZIP code не подсвечен красным"

        green_fields = [
            'first-name', 'last-name', 'address',
            'e-mail', 'phone', 'city',
            'country', 'job-position', 'company'
        ]

        for field_id in green_fields:
            field_element = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_element.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"

        print("Все проверки пройдены успешно!")

    finally:
        driver.quit()

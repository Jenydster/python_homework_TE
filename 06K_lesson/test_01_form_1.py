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
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        # Заполнение формы
        fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'job-position': "QA",
            'company': "SkyPro"
        }

        for name, value in fields.items():
            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"input[name='{name}']")
            ))
            element.clear()
            element.send_keys(value)

        submit_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#zip-code.alert-danger")
        ))

        # 1. Проверка ZIP code (красная подсветка)
        zip_code_field = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class"), \
            "Поле ZIP code не подсвечено красным"

        # 2. Проверка остальных полей (зеленая подсветка)
        green_fields = [
            'first-name', 'last-name', 'address',
            'e-mail', 'phone', 'city',
            'country', 'job-position', 'company'
        ]

        for field_id in green_fields:
            field_element = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_element.get_attribute("class"), \
                f"Поле {field_id} не подсвечено зеленым"

    finally:
        driver.quit()

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalcPage  # Исправленный импорт


@allure.feature("Тестирование калькулятора")
class TestCalculator:

    @allure.title("Проверка вычислений с задержкой")
    def test_delay_calculator(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        try:
            with allure.step("Открытие страницы калькулятора"):
                driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
                page = CalcPage(driver)

            with allure.step("Установка задержки 45 секунд"):
                page.set_delay(45)

            with allure.step("Выполнение операции 7 + 8"):
                page.safe_click("7")
                page.safe_click("+")
                page.safe_click("8")
                page.safe_click("=")

            with allure.step("Проверка результата"):
                page.wait_for_result(15)
                result = page.get_result()
                assert result == "15", f"Ожидался 15, получено {result}"

        finally:
            driver.quit()

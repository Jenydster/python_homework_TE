import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.calc_page import CalcPage


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора с задержкой."""

    @allure.title("Проверка вычислений с задержкой")
    @allure.description("Тест проверяет работу калькулятора с установленной задержкой 45 секунд")
    def test_delay_calculator(self) -> None:
        """Проверяет корректность вычислений калькулятора с задержкой."""
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        
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

            with allure.step("Ожидание результата и проверка"):
                page.wait_for_result(15)
                result = page.get_result()
                
                with allure.step(f"Проверка что результат равен 15 (фактический: {result})"):
                    assert result == "15", f"Ожидался 15, получено {result}"
        
        finally:
            driver.quit()
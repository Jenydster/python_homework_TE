from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


def test_delay_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        page = CalcPage(driver)

        # Устанавливаем задержку
        page.set_delay(45)

        # Нажимаем кнопки
        page.safe_click("7")
        page.safe_click("+")
        page.safe_click("8")
        page.safe_click("=")

        # Ждём результат
        page.wait_for_result(15)
        result = page.get_result()
        print("Результат:", result)

        assert result == "15", f"Ожидался 15, получено {result}"

    finally:
        driver.quit()


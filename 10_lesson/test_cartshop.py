import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage


@allure.feature("Тестирование интернет-магазина")
@allure.severity(allure.severity_level.CRITICAL)
class TestShop:
    """Тесты для интернет-магазина."""

    @allure.title("Проверка оформления заказа")
    @allure.description("Тест проверяет процесс оформления заказа и итоговую сумму")
    def test_shop_cart(self) -> None:
        """Проверяет процесс оформления заказа в интернет-магазине."""
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        
        try:
            with allure.step("Открытие страницы авторизации"):
                login_page = LoginPage(driver)
                login_page.open()

            with allure.step("Авторизация с учетными данными standard_user/secret_sauce"):
                login_page.login("standard_user", "secret_sauce")
            
            with allure.step("Добавление товаров в корзину"):
                main_page = MainPage(driver)
                products_to_add = [
                    "sauce-labs-backpack",
                    "sauce-labs-bolt-t-shirt",
                    "sauce-labs-onesie"
                ]
                
                for product in products_to_add:
                    with allure.step(f"Добавление товара {product} в корзину"):
                        main_page.add_product(product)
            
            with allure.step("Переход в корзину"):
                main_page.go_to_cart()
            
            with allure.step("Оформление заказа"):
                cart_page = CartPage(driver)
                cart_page.checkout()
            
            with allure.step("Заполнение информации для доставки"):
                checkout_page = CheckOutPage(driver)
                checkout_page.fill_info("Evgeniia", "Tuzhilova", "111111")
            
            with allure.step("Получение и проверка итоговой суммы"):
                total_value = checkout_page.get_total()
                
                with allure.step(f"Проверка что итоговая сумма равна 58.29 (фактическая: {total_value})"):
                    assert total_value == "58.29", f"Ожидалось 58.29, получено {total_value}"
        
        finally:
            driver.quit()
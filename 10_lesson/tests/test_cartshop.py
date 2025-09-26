import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page import LoginPage  # Исправленный импорт
from main_page import MainPage    # Исправленный импорт
from cart_page import CartPage    # Исправленный импорт
from checkout_page import CheckOutPage  # Исправленный импорт


@allure.feature("Тестирование интернет-магазина")
class TestShop:

    @allure.title("Проверка оформления заказа")
    def test_shop_cart(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        try:
            with allure.step("Авторизация в магазине"):
                login_page = LoginPage(driver)
                login_page.open()
                login_page.login("standard_user", "secret_sauce")

            with allure.step("Добавление товаров в корзину"):
                main_page = MainPage(driver)
                products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]
                for product in products:
                    main_page.add_product(product)
                main_page.go_to_cart()

            with allure.step("Оформление заказа"):
                cart_page = CartPage(driver)
                cart_page.checkout()

                checkout_page = CheckOutPage(driver)
                checkout_page.fill_info("Evgeniia", "Tuzhilova", "111111")

            with allure.step("Проверка итоговой суммы"):
                total_value = checkout_page.get_total()
                assert total_value == "58.29", f"Ожидалось 58.29, получено {total_value}"

        finally:
            driver.quit()

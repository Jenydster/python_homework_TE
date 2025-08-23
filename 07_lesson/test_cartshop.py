from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckOutPage import CheckOutPage


def test_shop_cart():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        main_page = MainPage(driver)
        products_to_add = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie"
        ]
        for product in products_to_add:
            main_page.add_product(product)
        main_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_page.checkout()
        
        checkout_page = CheckOutPage(driver)
        checkout_page.fill_info("Evgeniia", "Tuzhilova", "111111")
        
        total_value = checkout_page.get_total()
        assert total_value == "58.29", f"Ожидалось 58.29, получено {total_value}"
        
    finally:
        driver.quit()


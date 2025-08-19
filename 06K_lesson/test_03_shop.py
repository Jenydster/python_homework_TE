from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_shop_cart():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        driver.get("https://www.saucedemo.com/")
        input_user = "#user-name"
        un_input = driver.find_element(By.CSS_SELECTOR, input_user)
        un_input.send_keys("standard_user")

        input_password = "#password"
        password_input = driver.find_element(By.CSS_SELECTOR, input_password)
        password_input.send_keys("secret_sauce")

        driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        input_fn = "#first-name"
        fn_input = driver.find_element(By.CSS_SELECTOR, input_fn)
        fn_input.send_keys("Evgeniia")

        input_ln = "#last-name"
        ln_input = driver.find_element(By.CSS_SELECTOR, input_ln)
        ln_input.send_keys("Tuzhilova")

        input_zc = "#postal-code"
        zc_input = driver.find_element(By.CSS_SELECTOR, input_zc)
        zc_input.send_keys("111111")

        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        total_price = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        total_value = total_price.replace('Total: $', '').strip()
        assert total_value == "58.29", f"Ожидалось 58.29, получено {total_value}"
        print(total_value)

    finally:
        driver.quit()


test_shop_cart()

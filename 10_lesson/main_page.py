from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_id):
        self.driver.find_element(By.CSS_SELECTOR, f"#add-to-cart-{product_id}").click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

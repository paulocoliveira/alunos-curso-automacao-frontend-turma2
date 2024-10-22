from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsByCategory(BasePage):
    PRODUCTS = {
        28: (By.XPATH, "//a[@id='mz-product-grid-image-28-212408']"),
        29: (By.XPATH, "//a[@id='mz-product-grid-image-29-212408']"),
        30: (By.XPATH, "//a[@id='mz-product-grid-image-30-212408']")
    }

    def click_on_product(self, product_id):
        product_element = self.PRODUCTS.get(product_id)

        sleep(1)

        self.wait_for_element(product_element).click()
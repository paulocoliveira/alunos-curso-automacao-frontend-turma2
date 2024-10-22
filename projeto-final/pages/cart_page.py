from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//div[@id='content']/div[2]/a[2]")

    def click_checkout_button(self):
        self.wait_for_element(self.CHECKOUT_BUTTON).click()
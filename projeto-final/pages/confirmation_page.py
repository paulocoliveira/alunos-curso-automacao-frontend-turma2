from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage(BasePage):
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@id='button-confirm']")

    def click_confirm_order_button(self):
        self.wait_for_element(self.CONFIRM_ORDER_BUTTON).click()
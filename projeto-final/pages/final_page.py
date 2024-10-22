from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinalPage(BasePage):
    MESSAGE = (By.XPATH, "//div[@id='content']/h1")

    def get_message(self, message):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.MESSAGE, message)
        )

        return self.wait_for_element(self.MESSAGE).text
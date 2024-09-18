from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class FinalPage(BasePage):
    AGRADECIMENTO_MSG = (By.XPATH, "//h2")

    def obter_mensagem(self):
        return self.wait_for_element(self.AGRADECIMENTO_MSG).text
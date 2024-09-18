from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from pages.base_page import BasePage
from time import sleep

class FinalPage(BasePage, PageFactory):
    
    locators = {
        "agradecimento_msg": (By.XPATH, "//h2")
    }
    
    def obter_mensagem(self):
        return self.agradecimento_msg.get_text()
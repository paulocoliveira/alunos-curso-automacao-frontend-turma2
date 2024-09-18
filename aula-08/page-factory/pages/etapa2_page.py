from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from seleniumpagefactory import PageFactory
from time import sleep

class Etapa2Page(BasePage, PageFactory):

    locators = {
        "trabalha_area": (By.ID, "trabalhaArea"),
        "experiencia": (By.ID, "experiencia"),
        "empresa": (By.ID, "empresa"),
        "botao_prosseguir": (By.XPATH, "//button")
    }

    def preencher_etapa2(self, trabalha_area, experiencia, empresa):
        self.trabalha_area.set_text(trabalha_area)
        self.experiencia.set_text(experiencia)
        self.empresa.set_text(empresa)
        sleep(3)
        self.botao_prosseguir.click_button()

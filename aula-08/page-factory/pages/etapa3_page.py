from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from pages.base_page import BasePage
from time import sleep

class Etapa3Page(BasePage, PageFactory):

    locators = {
        "interesse_mentoria": (By.ID, "interesseMentoria"),
        "descricao": (By.ID, "descricao"),
        "botao_enviar": (By.XPATH, "//button")
    }

    def preencher_etapa3(self, interesse_mentoria, descricao):
        self.interesse_mentoria.set_text(interesse_mentoria)
        self.descricao.set_text(descricao)
        sleep(3)
        self.botao_enviar.click_button()

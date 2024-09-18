from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class Etapa1Page(BasePage, PageFactory):

    locators = {
        "nome": (By.ID, "nome"),
        "email": (By.ID, "email"),
        "idade": (By.ID, "idade"),
        "whatsapp": (By.ID, "whatsapp"),
        "cidade": (By.ID, "cidade"),
        "botao_prosseguir": (By.XPATH, "//button")
    }

    def preencher_etapa1(self, nome, email, idade, whatsapp, cidade):
        self.nome.set_text(nome)
        self.email.set_text(email)
        self.idade.set_text(idade)
        self.whatsapp.set_text(whatsapp)
        self.cidade.set_text(cidade)
        sleep(3)
        self.botao_prosseguir.click_button()

    def preencher_nome(self, nome):
        self.nome.set_text(nome)
    
    def preencher_email(self, email):
        self.email.set_text(email)
    
    def preencher_idade(self, idade):
        self.idade.set_text(idade)

    def preencher_whatsapp(self, whatsapp):
        self.whatsapp.set_text(whatsapp)

    def preencher_cidade(self, cidade):
        self.cidade.set_text(cidade)
    
    def clicar_no_botao_prosseguir(self):
        self.botao_prosseguir.click_button()
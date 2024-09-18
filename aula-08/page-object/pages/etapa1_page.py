from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Etapa1Page(BasePage):
    NOME = (By.ID, "nome")
    EMAIL = (By.ID, "email")
    IDADE = (By.ID, "idade")
    WHATSAPP = (By.ID, "whatsapp")
    CIDADE = (By.ID, "cidade")
    BOTAO_PROSSEGUIR = (By.XPATH, "//button")

    def preencher_etapa1(self, nome, email, idade, whatsapp, cidade):
        self.wait_for_element(self.NOME).send_keys(nome)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.IDADE).send_keys(idade)
        self.driver.find_element(*self.WHATSAPP).send_keys(whatsapp)
        self.driver.find_element(*self.CIDADE).send_keys(cidade)
        sleep(3)
        self.driver.find_element(*self.BOTAO_PROSSEGUIR).click()

    def preencher_nome(self, nome):
        self.wait_for_element(self.NOME).send_keys(nome)
    
    def preencher_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
    
    def preencher_idade(self, idade):
        self.driver.find_element(*self.IDADE).send_keys(idade)

    def preencher_whatsapp(self, whatsapp):
        self.driver.find_element(*self.WHATSAPP).send_keys(whatsapp)

    def preencher_cidade(self, cidade):
        self.driver.find_element(*self.CIDADE).send_keys(cidade)
    
    def clicar_no_botao_prosseguir(self):
        self.driver.find_element(*self.BOTAO_PROSSEGUIR).click()
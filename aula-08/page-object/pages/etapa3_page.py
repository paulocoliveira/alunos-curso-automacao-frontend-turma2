from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from time import sleep

class Etapa3Page(BasePage):
    INTERESSE_MENTORIA = (By.ID, "interesseMentoria")
    DESCRIÇÃO = (By.ID, "descricao")
    BOTÃO_ENVIAR = (By.XPATH, "//button")

    def preencher_etapa3(self, interesse_mentoria, descricao):
        self.wait_for_element(self.INTERESSE_MENTORIA)
        select_interesse_mentoria = Select(self.driver.find_element(*self.INTERESSE_MENTORIA))
        select_interesse_mentoria.select_by_value(interesse_mentoria)
        self.driver.find_element(*self.DESCRIÇÃO).send_keys(descricao)
        sleep(3)
        self.driver.find_element(*self.BOTÃO_ENVIAR).click()

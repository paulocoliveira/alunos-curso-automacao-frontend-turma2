from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from time import sleep

class Etapa2Page(BasePage):
    TRABALHA_AREA = (By.ID, "trabalhaArea")
    EXPERIENCIA = (By.ID, "experiencia")
    EMPRESA = (By.ID, "empresa")
    BOTÃO_PROSSEGUIR = (By.XPATH, "//button")

    def preencher_etapa2(self, trabalha_area, experiencia, empresa):
        self.wait_for_element(self.TRABALHA_AREA)
        select_trabalha_area = Select(self.driver.find_element(*self.TRABALHA_AREA))
        select_trabalha_area.select_by_value(trabalha_area)
        self.driver.find_element(*self.EXPERIENCIA).send_keys(experiencia)
        self.driver.find_element(*self.EMPRESA).send_keys(empresa)
        sleep(3)
        self.driver.find_element(*self.BOTÃO_PROSSEGUIR).click()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page import BasePage
from pages.etapa1_page import Etapa1Page
from pages.etapa2_page import Etapa2Page
from pages.etapa3_page import Etapa3Page
from pages.final_page import FinalPage

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    
    BasePage(driver).open_site()

    yield driver

    driver.quit()

def test_complete_registration(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Zélia Silva", "zelia@silva.pt", "15", "+3519998877", "Gondomar")

    etapa2 = Etapa2Page(driver)
    etapa2.preencher_etapa2("sim_desempregado", "5", "Expert QA Academy")

    etapa3 = Etapa3Page(driver)
    etapa3.preencher_etapa3("automacao_testes", "Preciso urgente aprender Python e Selenium")

    final = FinalPage(driver)
    msg = final.obter_mensagem()

    assert msg == "Obrigado pela sua inscrição!"

    sleep(5)

def atest_complete_registration_etapa1_separated_functions(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_nome("Aline Soares")
    etapa1.preencher_email("aline@soares.pt")
    etapa1.preencher_idade("16")
    etapa1.preencher_whatsapp("999888777")
    etapa1.preencher_cidade("Rebordosa")
    sleep(3)
    etapa1.clicar_no_botao_prosseguir()

    etapa2 = Etapa2Page(driver)
    etapa2.preencher_etapa2("sim_desempregado", "5", "Expert QA Academy")

    etapa3 = Etapa3Page(driver)
    etapa3.preencher_etapa3("automacao_testes", "Preciso urgente aprender Python e Selenium")

    final = FinalPage(driver)
    msg = final.obter_mensagem()

    assert msg == "Obrigado pela sua inscrição!"

def atest_only_name(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_nome("Aline Soares")
    sleep(3)
    etapa1.clicar_no_botao_prosseguir()

    #falta adicionar um assert

def atest_only_email(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_email("aline@soares.pt")
    sleep(3)
    etapa1.clicar_no_botao_prosseguir()

    #falta adicionar um assert

def atest_invalid_email(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_email("meuemailinvalido")
    sleep(3)
    etapa1.clicar_no_botao_prosseguir()

    #falta adicionar um assert

def atest_empty_email(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_email("")
    sleep(3)
    etapa1.clicar_no_botao_prosseguir()
    
    #falta adicionar um assert
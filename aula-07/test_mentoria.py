from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page import BasePage
from pages.etapa1_page import Etapa1Page

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

    sleep(5)

def test_only_with_name(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Zélia Silva", "", "", "", "")

    sleep(5)

def test_without_filling(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("", "", "", "", "")

    sleep(5)
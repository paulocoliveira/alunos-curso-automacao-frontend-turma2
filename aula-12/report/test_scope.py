import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def load_config():
    print("\n Carregando configuração global para todos os testes.")
    config = {
        "url": "https://www.google.com",
        "db": "test_db"
    }
    return config

@pytest.fixture(scope="module")
def driver(load_config):
    print("\n Iniciando o navegador para os testes do módulo.")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get(load_config["url"])
    driver.maximize_window()

    yield driver

    print("\n Fechando o navegador aberto para os testes do módulo.")
    driver.quit()

@pytest.fixture(scope="class")
def database_config(load_config):
    print("\n Conectando ao banco de dados para os testes da classe.")
    db_connection = load_config["db"]
    yield db_connection
    print("\n Desconectando do banco de dados que estava conectado para os testes da classe.")

@pytest.fixture(scope="function")
def clean_data():
    print("\n Resetando os dados para o teste.")

@pytest.mark.usefixtures("database_config")
class TestDataBase:
    def test_data_3(self, driver):
        print("\n Teste de dados 3.")

    def test_data_4(self, driver):
        print("\n Teste de dados 4.")

def test_data_1(clean_data):
    print("\n Teste de dados 1.")

def test_data_2(clean_data):
    print("\n Teste de dados 2.")
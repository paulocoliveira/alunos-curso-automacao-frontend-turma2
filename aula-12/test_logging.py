from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from datetime import datetime, timedelta
import logging
import functools

logger = logging.getLogger(__name__)

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL', 'driver': 'ALL'})
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[text()='DateTime']").click()

    yield driver

    logs = driver.get_log("browser")

    for log in logs:
       logger.info("Log do Navegador: %s", log)

    driver.quit()

def log_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("Erro durante o teste: %s", e, exc_info=True)
            raise
    return wrapper

@log_exception
def test_datetime_manipulation_1(driver):
   current_time = datetime.now()

   driver.find_element(By.ID, "current_time").send_keys(str(current_time))
   
   # caso esteja rodando no windows substituir o %-m por %#m
   formatted_1 = current_time.strftime("%d-%-m-%y")

   driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)

   formatted_2 = current_time.strftime("%Y-%m-%d %H:%M:%S")

   driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)

   # caso queira voltar no tempo, use os dias com o sinal negativo antes
   # caso precise voltar em anos, faça a multiplicação 365*anos e use em dias
   # ex: se quiser voltar 120 anos, usar como abaixo 
   # date_in_60_days = current_time + timedelta(days=-43800)
   date_in_60_days = current_time + timedelta(days=60)

   formatted_3 = date_in_60_days.strftime("%d-%m-%y")

   driver.find_element(By.ID, "date_in_60_days").send_keys(formatted_3)

   in_2099 = current_time.replace(year=2099)

   formatted_4 = in_2099.strftime("%d-%m-%Y")

   driver.find_element(By.ID, "year_2099").send_keys(formatted_4)

   driver.find_element(By.XPATH, "//button[text()='CONCLUIR']").click()

   logger.info("Finalizei a execução do teste 1")

   sleep(3)

@log_exception
def test_datetime_manipulation_2(driver):
   current_time = datetime.now()

   driver.find_element(By.ID, "current_time").send_keys(str(current_time))
   
   # caso esteja rodando no windows substituir o %-m por %#m
   formatted_1 = current_time.strftime("%d-%-m-%y")

   driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)

   formatted_2 = current_time.strftime("%Y-%m-%d %H:%M:%S")

   driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)

   # caso queira voltar no tempo, use os dias com o sinal negativo antes
   # caso precise voltar em anos, faça a multiplicação 365*anos e use em dias
   # ex: se quiser voltar 120 anos, usar como abaixo 
   # date_in_60_days = current_time + timedelta(days=-43800)
   date_in_60_days = current_time + timedelta(days=60)

   formatted_3 = date_in_60_days.strftime("%d-%m-%y")

   driver.find_element(By.ID, "date_in_60_days").send_keys(formatted_3)

   in_2099 = current_time.replace(year=2099)

   formatted_4 = in_2099.strftime("%d-%m-%Y")

   driver.find_element(By.ID, "year_2099").send_keys(formatted_4)

   driver.find_element(By.XPATH, "//button[text()='FINALIZAR']").click()

   logger.info("Finalizei a execução do teste 2")

   sleep(3)

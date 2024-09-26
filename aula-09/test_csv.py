from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import csv

csv_file_name = "users.csv"

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[text()='CSV']").click()

    yield driver

    driver.quit()

def test_fill_form_from_csv(driver):
    with open(csv_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for nome, sobrenome, email in reader:
            driver.find_element(By.ID, "nome").send_keys(nome)
            driver.find_element(By.ID, "sobrenome").send_keys(sobrenome)
            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.XPATH, "//button").click()
            sleep(1)
        sleep(5)
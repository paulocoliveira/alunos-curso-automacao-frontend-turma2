from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import json

@pytest.fixture(scope="session")
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

def load_user_data():
    with open("users.json") as jsonfile:
        return json.load(jsonfile)

@pytest.mark.parametrize("user", load_user_data())
def test_fill_form_from_json(driver, user):
    driver.find_element(By.ID, "nome").send_keys(user["Nome"])
    driver.find_element(By.ID, "sobrenome").send_keys(user["Sobrenome"])
    driver.find_element(By.ID, "email").send_keys(user["Email"])
    driver.find_element(By.XPATH, "//button").click()
    sleep(1)
sleep(5)
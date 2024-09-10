from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    #driver.implicitly_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/waits/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def atest_implicity_wait(driver):
    button = driver.find_element(By.XPATH, "//section[@id='conditional-element-section']/button")
    button.click()
    hidden_button = driver.find_element(By.ID, "hidden-button")
    hidden_button.click()

def test_file_upload(driver):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "qrcode.png")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )

    driver.find_element(By.ID, "file-upload").send_keys(file_path)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Enviar Arquivo')]").click()

    message_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "file-upload-status"))
    )

    assert message_element.text == "Arquivo enviado"

    sleep(10)
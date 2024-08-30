from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()

def test_check_title_google(driver):
    driver.get("https://www.google.com")
    title = driver.title
    assert title == "Google"

    sleep(3)

def test_check_title_eqa(driver):
    driver.get("https://www.worten.pt/")
    title = driver.title
    assert title == "Worten - Tudo o que precisas em Worten.pt"
    

    sleep(3)

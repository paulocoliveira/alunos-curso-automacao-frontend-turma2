from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def driver(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        my_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=my_service, options=chrome_options)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser não configurado!")

    yield driver

    driver.quit()

def test_open_google(driver):
    driver.get("https://www.google.com")
    sleep(5)

def test_open_linkedin(driver):
    driver.get("https://www.linkedin.com")
    sleep(5)
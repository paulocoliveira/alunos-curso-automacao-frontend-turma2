from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


@pytest.fixture()
def driver():
    browser_choice = config.get("default", "browser")
    if browser_choice == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        my_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=my_service, options=chrome_options)
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser não configurado!")

    url_to_be_opened = config.get("default", "url")
    driver.get(url_to_be_opened)
    
    driver.maximize_window()

    yield driver

    driver.quit()

def test_print_page_title(driver):
    print(driver.title)
    sleep(10)
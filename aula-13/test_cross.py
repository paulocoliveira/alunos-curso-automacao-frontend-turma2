from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from datetime import datetime, timedelta
import json
import os

def load_data():
    with open("environment.json") as jsonfile:
        return json.load(jsonfile)

@pytest.fixture(params=load_data(), scope="function")
def driver(request):
    env = request.param
    plataform = env["platform"]
    browser = env["browser"]
    
    if browser == "Chrome":
        specific_browser_option = webdriver.ChromeOptions()
        specific_browser_option.add_argument("--disable-search-engine-choice-screen")
    elif browser == "Firefox":
        specific_browser_option = webdriver.FirefoxOptions()
    elif browser == "MicrosoftEdge":
        specific_browser_option = webdriver.EdgeOptions()
    elif browser == "Safari":
        specific_browser_option = webdriver.SafariOptions()
    
    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_ACCESS_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"
    
    lt_options = {
        "user": username,
        "acessKey": accessToken,
        "build": "Version 5.0",
        "name": "Cross-browser testing",
        "platformName": plataform,
        "browserName": browser,
        "browserVersion": "latest",
        "selenium_version": "latest",
        "w3c": True,
        "visual": True
    }
    
    options = specific_browser_option
    options.set_capability("LT:Options", lt_options)
    
    url = "https://" + username + ":" + accessToken + "@" + gridUrl
    # A url acima ficaria algo do tipo: "https://seuusuario:suakey@hub.lambdatest.com/wd/hub"
    
    driver = webdriver.Remote(
        command_executor = url,
        options = options
    )
    
    driver.maximize_window()
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.find_element(By.XPATH, "//button[text()='DateTime']").click()
    
    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver.execute_script("lambda-status=failed")
    else:
        driver.execute_script("lambda-status=passed")

    driver.quit()

def test_datetime_manipulation_1(driver):
    current_time = datetime.now()

    driver.find_element(By.ID, "current_time").send_keys(str(current_time))

    formatted_1 = current_time.strftime("%d-%#m-%y")

    driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)

    formatted_2 = current_time.strftime("%Y-%m-%d %H:%M:%S")

    driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)

    date_in_60_days = current_time + timedelta(days=60)

    formatted_3 = date_in_60_days.strftime("%d-%m-%y")

    driver.find_element(By.ID, "date_in_60_days").send_keys(formatted_3)

    in_2099 = current_time.replace(year=2099)

    formatted_4 = in_2099.strftime("%d-%m-%Y")

    driver.find_element(By.ID, "year_2099").send_keys(formatted_4)

    driver.find_element(By.XPATH, "//button[text()='CONCLUIR']").click()

    sleep(3)

def test_datetime_manipulation_2(driver):
    current_time = datetime.now()

    driver.find_element(By.ID, "current_time").send_keys(str(current_time))

    formatted_1 = current_time.strftime("%d-%#m-%y")

    driver.find_element(By.ID, "formatted_date1").send_keys(formatted_1)

    formatted_2 = current_time.strftime("%Y-%m-%d %H:%M:%S")

    driver.find_element(By.ID, "formatted_date2").send_keys(formatted_2)

    date_in_60_days = current_time + timedelta(days=60)

    formatted_3 = date_in_60_days.strftime("%d-%m-%y")

    driver.find_element(By.ID, "date_in_60_days").send_keys(formatted_3)

    in_2099 = current_time.replace(year=2099)

    formatted_4 = in_2099.strftime("%d-%m-%Y")

    driver.find_element(By.ID, "year_2099").send_keys(formatted_4)

    driver.find_element(By.XPATH, "//button[text()='CONCLUIR']").click()

    sleep(3)

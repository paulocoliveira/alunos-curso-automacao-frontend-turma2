from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from strategies.regular_user_test_strategy import RegularUserTestStrategy
from strategies.admin_user_test_strategy import AdminUserTestStrategy
from strategies.super_admin_user_test_strategy import SuperAdminUserTestStrategy

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/login/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_regular_user_behaviour(driver):
    strategy = RegularUserTestStrategy(driver)
    strategy.execute_test()

def test_regular_user_behaviour(driver):
    strategy = RegularUserTestStrategy(driver)
    strategy.login("aline")
    strategy.verify_home_page_message()
    strategy.logout()

def test_admin_user_behaviour(driver):
    strategy = AdminUserTestStrategy(driver)
    strategy.execute_test()

def test_super_admin_user_behaviour(driver):
    strategy = SuperAdminUserTestStrategy(driver)
    strategy.execute_test()
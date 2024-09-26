from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import locale

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[text()='Locale']").click()

    yield driver

    driver.quit()

def test_locale_manipulation(driver):
   current_locale = locale.getlocale()

   driver.find_element(By.ID, "current_locale").send_keys(str(current_locale))

   new_locale = "es_es.UTF-8"

   locale.setlocale(locale.LC_ALL, new_locale)

   updated_locale = locale.getlocale()

   driver.find_element(By.ID, "new_locale").send_keys(str(updated_locale))

   formatted_currency = locale.currency(123456789, symbol=True, grouping=True)

   print(formatted_currency)

   driver.find_element(By.ID, "formatted_number").send_keys(str(formatted_currency))

   sleep(20)

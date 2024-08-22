from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

my_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=my_service, options=chrome_options)

# Accessing first site
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

browser.maximize_window()

# By ID
email = browser.find_element(By.ID, "input-email")

# By NAME
password = browser.find_element(By.NAME, "password")

# Accessing second site
browser.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

# By CLASS_NAME
button = browser.find_element(By.CLASS_NAME, "btn-dark")

# Accessing third site
browser.get("https://www.lambdatest.com/selenium-playground/")

# By LINK_TEXT
ajax_link = browser.find_element(By.LINK_TEXT, "Ajax Form Submit")

# By PARTIAL_LINK_TEXT
code_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Codes")

# By TAG_NAME
links = browser.find_elements(By.TAG_NAME, "a")

sleep(5)
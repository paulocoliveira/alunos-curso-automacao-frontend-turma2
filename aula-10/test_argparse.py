from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import argparse

parse = argparse.ArgumentParser(description="Selenium Test Script Configuration")
parse.add_argument("--url", required=True, help="URL a ser aberta")
parse.add_argument("--browser", required=True, help="Browser para execução")

args = parse.parse_args()

url = args.url
browser = args.browser

if browser == "chrome":
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
elif browser == "firefox":
    driver = webdriver.Firefox()
else:
    raise ValueError("Browser não configurado!")

driver.maximize_window()
driver.get(url)

print(driver.title)

sleep(5)

driver.quit()
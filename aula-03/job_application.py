from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

my_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=my_service, options=chrome_options)

browser.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

browser.maximize_window()

full_name = browser.find_element(By.XPATH, "//input[@id='fullName']")
full_name.send_keys("Aline Pereira")

email = browser.find_element(By.XPATH, "//input[@name='email']")
email.send_keys("aline.pereira@aline.pt")

phone = browser.find_element(By.XPATH, "//input[@type='tel']")
phone.send_keys("999888777")

Select(browser.find_element(By.XPATH, "//select[@id='desiredPosition']")).select_by_visible_text("QA")

remote = browser.find_element(By.XPATH, "//input[@value='remote']")
remote.click()

years = browser.find_element(By.XPATH, "//input[@name='experienceYears']")
years.send_keys("3")

html = browser.find_element(By.XPATH, "//input[@id='skill1']")
html.click()

js = browser.find_element(By.XPATH, "//input[@id='skill3']")
js.click()

# skills = browser.find_elements(By.XPATH, "//input[contains(@id,'skill')]")
# skills[0].click()
# skills[2].click()

button = browser.find_element(By.XPATH, "//button")
button.click()

message = browser.find_element(By.XPATH, "//span[@id='successMessage']").text

assert message == "Submission successful!"

sleep(5)
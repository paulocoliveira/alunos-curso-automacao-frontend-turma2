from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_full_form(driver):
    full_name = driver.find_element(By.ID, "fullName")
    full_name.send_keys("Aline Pereira")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("aline.pereira@aline.pt")

    phone = driver.find_element(By.ID, "phoneNumber")
    phone.send_keys("999888777")

    Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("QA")

    remote = driver.find_element(By.ID, "location1")
    remote.click()

    years = driver.find_element(By.NAME, "experienceYears")
    years.send_keys("3")

    html = driver.find_element(By.ID, "skill1")
    html.click()

    js = driver.find_element(By.ID, "skill3")
    js.click()

    # skills = driver.find_elements(By.NAME, "skill")
    # skills[0].click()
    # skills[2].click()

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    assert message == "Submission successful!"

    sleep(5)

def test_only_fullname(driver):
    full_name = driver.find_element(By.ID, "fullName")
    full_name.send_keys("Aline Pereira")

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    assert message == "Submission successful!"

    sleep(5)

def test_without_filling(driver):
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    assert message == "Submission successful!"

    sleep(5)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import random

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[text()='Random']").click()

    yield driver

    driver.quit()

def get_programming_language_buttons(driver):
    return driver.find_elements(By.XPATH, "//div[@class='button-grid']/button")

#random.random() - entre 0.0 (incluído) e 1.0(não incluído)
def atest_random_click(driver):
    buttons = get_programming_language_buttons(driver)

    for _ in range(5):
        random_number = random.random()
        button_index = int(random_number * len(buttons))
        buttons[button_index].click()
        sleep(2)

#random.randint(a, b) - entre a (incluído) e b (incluído) 
def atest_random_int_click(driver):
    buttons = get_programming_language_buttons(driver)

    for _ in range(5):
        button_index = random.randint(0, len(buttons)-1)
        buttons[button_index].click()
        sleep(2)

#random.choice(seq) - item aleatório em uma lista
def atest_random_choice_click(driver):
    buttons = get_programming_language_buttons(driver)
    for _ in range(5):
        random_button = random.choice(buttons)
        random_button.click()
        sleep(1)

#random.shuffle(seq) - embaralha a lista original
def atest_random_shuffle_click(driver):
    buttons = get_programming_language_buttons(driver)
    random.shuffle(buttons)
    for button in buttons[:5]:
        button.click()
        sleep(1)

#random.sample(population, k) - retorna uma amostra aleatória de k elementos
def atest_random_sample_click(driver):
    buttons = get_programming_language_buttons(driver)
    sample_buttons = random.sample(buttons, 5)
    for button in sample_buttons:
        button.click()
        sleep(1)

#random.randrange(start, stop, step) - start (incluído) até o stop (não inclído), 
# step (opcional) é o intervalo entre os números
def atest_randrange_click(driver):
    buttons = get_programming_language_buttons(driver)
    for _ in range(5):
        random_index = random.randrange(0, len(buttons), 2)
        buttons[random_index].click()
        sleep(1)

#random.uniform(a, b) - número de ponto flutuante no intervalo de a (incluído) e b (incluído)
def test_random_uniform_click(driver):
    buttons = get_programming_language_buttons(driver)
    for _ in range(5):
        random_index = int(random.uniform(0, len(buttons)))
        buttons[random_index].click()
        sleep(1)
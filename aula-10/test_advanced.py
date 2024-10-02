from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver import ActionChains


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/advanced/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_slider_interaction(driver):
    slider = driver.find_element(By.ID, "range-slider")
    slider_value = driver.find_element(By.ID, "slider-value")
    slider_size = slider.size["width"]

    target_value = 75
    current_value = int(slider.get_attribute("value"))
    offset = int(slider_size * (target_value - current_value) / 99)

    actions = ActionChains(driver)
    actions.move_to_element_with_offset(slider, 0, 0)
    actions.click_and_hold()
    actions.move_by_offset(offset, 0)
    actions.release()
    actions.perform()

    sleep(10)

    final_value = int(slider_value.text)

    assert target_value - 1 <= final_value <= target_value + 1

    # rascunho
    # largura = 2000
    # 100 valores e cada um representa largura / 100 = 20

    # target_value = 75
    # slider_size * (target_value - current_value) / 99

    # 2000 * (75 - 50) / 99
    # 2000 * 25 / 99
    # 50000 / 99 = -505,05

def test_switch_interaction(driver):
    switch = driver.find_element(By.ID, "switch")
    button = driver.find_element(By.ID, "toggle-button")

    sleep(2)

    assert not button.is_enabled()

    driver.execute_script("arguments[0].click()", switch)

    assert button.is_enabled()

    sleep(5)

def test_iframe_interaction(driver):

    my_frame = driver.find_element(By.ID, "example-frame")
    driver.switch_to.frame(my_frame)

    driver.find_element(By.ID, "nickname").send_keys("Zélia")

    driver.find_element(By.ID, "confirm-button").click()

    message = driver.find_element(By.ID, "confirmation-message").text

    assert message == "Pronto! Deu tudo certo, Zélia!"

    driver.switch_to.default_content()

    driver.find_element(By.ID, "final-button").click()

    sleep(10)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_mandatory_scenario(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    products = driver.find_elements(By.XPATH, "//button[contains(@id, 'add-to-cart')]")

    for product in products:
        product.click()
    
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert badge.text == "6"

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    product_to_remove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    product_to_remove.click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "5"

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Karine")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Bueno")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("998877")

    continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    continue_button.click()

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")

    assert confirmation_message.text == "Thank you for your order!"

    sleep(3)

def test_price_sorting(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_visible_text("Price (low to high)")

    products_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    prices = []

    for product in products_price:
        price = product.text
        price = price.replace("$","")
        price = float(price)
        prices.append(price)
    
    sorted_prices = sorted(prices)

    assert prices == sorted_prices

def test_locked_user(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    sleep(3)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")

    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

def test_total_price(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    products = driver.find_elements(By.XPATH, "//button[contains(@id, 'add-to-cart')]")

    for product in products:
        product.click()

    products_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    total = 0

    for product in products_price:
        price = product.text
        price = price.replace("$","")
        price = float(price)
        total = total + price
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Karine")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Bueno")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("998877")

    continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    continue_button.click()

    total_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text

    total_list = total_price.split("$")
    total_value = total_list[1]
    total_value_float = float(total_value)

    assert total == total_value_float


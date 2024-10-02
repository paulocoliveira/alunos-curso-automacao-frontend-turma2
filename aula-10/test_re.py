from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import re

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/text/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_interactions(driver):
    text_data = """  
        Transaçtion Code: VJFI-674623, Phone: (59) 66301406
        Transaction Code: EIMZ-898724, Email: ybejhfyq@example.com
        Transaction Code: TSFW-655188, Email: wgvpeypbp@demo.net
        Transaction Code: UTNS-044799, Email: wvoav@test.org, Phone: (77) 84962052
        Transaction Code: HHMV-273514
        Transaction Code: KEMB-337781, Email: wrlvrzppvk@sample.edu, Phone: (42) 26467422
        Transaction Code: ZTWI-206815, Email: lrmqo@example.com, Phone: (76) 52291804
    """

    input_element = driver.find_element(By.ID, "inputText")
    button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")

    # re.match: Verifica se o padrão aparece no início da string.
    if re.match(r'Transaction Code: \w+-\d+', text_data.strip()):
        print("O texto começa com um código de transação válida")
    else:
        print("O texto NÃO começa com um código de transação válida")

    # re.search: Procura um padrão em toda a string e retorna o primeiro match
    phone = re.search(r'\(\d{2}\) \d{8}', text_data)

    if phone:
        print(phone.group())
        input_element.send_keys(phone.group())
        button.click()
    
    sleep(5)

    # re.findall: Procura todos os matches de um padrão em uma string e retorna uma list com as correspondências encontradas
    transaction_codes = re.findall(r'\w{4}-\d{6}', text_data)

    for code in transaction_codes:
        input_element.send_keys(code)
        button.click()
        sleep(1)

    input_element.send_keys("------")
    button.click()

    # re.compile: Compila um padrão de expressão regular em um objeto regex que eu posso reutilizar
    transaction_code_pattern = re.compile(r'\w{4}-\d{6}')

    codes = transaction_code_pattern.findall(text_data)

    for code in codes:
        input_element.send_keys(code)
        button.click()
        sleep(1)
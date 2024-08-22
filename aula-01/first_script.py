from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get("https://www.uol.com.br")

browser.maximize_window()

title = browser.title
print(title)

sleep(10)

browser.quit()
from time import sleep
from selenium.webdriver.common.by import By
from abc import ABC, abstractmethod

class UserTestStrategy(ABC):
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username):
        username_input = self.driver.find_element(By.ID, "username")
        username_input.send_keys(username)
        sleep(3)
        login_button = self.driver.find_element(By.XPATH, "//button")
        login_button.click()
    
    def logout(self):
        logout = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout.click()

    @abstractmethod
    def verify_home_page_message(self):
        pass
    
    def execute_test(self):
        self.login(self.username)
        sleep(3)
        self.verify_home_page_message()
        self.logout()
        sleep(2)

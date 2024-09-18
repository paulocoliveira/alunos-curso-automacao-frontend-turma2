from strategies.user_test_strategy import UserTestStrategy
from selenium.webdriver.common.by import By

class AdminUserTestStrategy(UserTestStrategy):
    username = "admin"

    def verify_home_page_message(self):
        msg = self.driver.find_element(By.ID, "message").text
        assert msg == "Bem-vindo, administrador!"
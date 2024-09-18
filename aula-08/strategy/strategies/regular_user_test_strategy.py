from strategies.user_test_strategy import UserTestStrategy
from selenium.webdriver.common.by import By

class RegularUserTestStrategy(UserTestStrategy):
    username = "aline"

    def verify_home_page_message(self):
        msg = self.driver.find_element(By.ID, "message").text
        assert msg == "Bem-vindo, usuário!"
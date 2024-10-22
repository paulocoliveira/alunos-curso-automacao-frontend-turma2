from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ProductPage(BasePage):
    AVAILABILITY = (By.XPATH, "//div[@id='entry_216826']//li[3]//span[2]")
    REVIEWS_TAB = (By.XPATH, "(//div[@id='entry_216814']//a)[2]")
    REVIEWS_MESSAGE = (By.XPATH, "//div[@id='mz-design-tab-216814-2']//p")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@id='entry_216842']/button")
    NOTIFICATION_VIEW_CART_BUTTON = (By.XPATH, "//div[@class='form-row']//div[1]/a")

    def get_availability_status(self):
        return self.wait_for_element(self.AVAILABILITY).text

    def click_review_tab(self):
        self.wait_for_element(self.REVIEWS_TAB).click()
    
    def get_reviews_tab_message(self):
        return self.wait_for_element(self.REVIEWS_MESSAGE).text

    def click_add_to_cart_button(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()
    
    def click_notification_view_cart_button(self):
        self.wait_for_element(self.NOTIFICATION_VIEW_CART_BUTTON).click()
        
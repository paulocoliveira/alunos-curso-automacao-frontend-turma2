from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    BANNER = (By.XPATH, "//div[@class='carousel-inner']/div[1]/a")
    SECOND_UNDER_99_PRODUCT = (By.XPATH, "//a[@id='mz-product-listing-image-81217990-0-1']")
    CATEGORY_MENU = (By.XPATH, "//div[@id='entry_217832']/a")
    CAMERA_SUBMENU = (By.XPATH, "//div[@id='widget-navbar-217841']//li[2]/a")

    def click_first_banner(self):
        self.wait_for_element(self.BANNER).click()
    
    def click_second_under_99_product(self):
        self.wait_for_element(self.SECOND_UNDER_99_PRODUCT).click()
    
    def click_category_menu(self):
        self.wait_for_element(self.CATEGORY_MENU).click()
    
    def click_camera_submenu(self):
        sleep(1)
        self.wait_for_element(self.CAMERA_SUBMENU).click()
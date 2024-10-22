from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    GUEST_CHECKOUT_OPTION = (By.XPATH, "//label[@for='input-account-guest']")
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    TELEPHONE = (By.ID, "input-payment-telephone")
    COMPANY = (By.ID, "input-payment-company")
    ADDRESS_1 = (By.ID, "input-payment-address-1")
    ADDRESS_2 = (By.ID, "input-payment-address-2")
    CITY = (By.ID, "input-payment-city")
    POSTAL_CODE = (By.ID, "input-payment-postcode")
    COUNTRY = (By.ID, "input-payment-country")
    REGION = (By.ID, "input-payment-zone")
    TERMS = (By.XPATH, "//label[@for='input-agree']")
    CONTINUE = (By.ID, "button-save")

    def click_guest_checkout_option(self):
        self.wait_for_element(self.GUEST_CHECKOUT_OPTION).click()
    
    def fill_personal_details(self, name, last_name, email, phone):
        self.wait_for_element(self.FIRST_NAME).send_keys(name)
        self.wait_for_element(self.LAST_NAME).send_keys(last_name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.TELEPHONE).send_keys(phone)
    
    def fill_billing_details(self, company, address1, address2, city, postalcode, country, region):
        self.wait_for_element(self.COMPANY).send_keys(company)
        self.wait_for_element(self.ADDRESS_1).send_keys(address1)
        self.wait_for_element(self.ADDRESS_2).send_keys(address2)
        self.wait_for_element(self.CITY).send_keys(city)
        self.wait_for_element(self.POSTAL_CODE).send_keys(postalcode)
        Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text(country)

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.REGION, region)
        )

        Select(self.driver.find_element(*self.REGION)).select_by_visible_text(region)
    
    def click_terms(self):
        self.wait_for_element(self.TERMS).click()
    
    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.CONTINUE))
        )
        
        continue_button.click()
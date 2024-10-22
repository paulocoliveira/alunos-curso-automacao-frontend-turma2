from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_detail_page import ProductPage
from pages.products_by_category import ProductsByCategory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.final_page import FinalPage

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    
    BasePage(driver).open_site()

    yield driver

    driver.quit()

def test_out_of_stock(driver):
    # acessar a mainpage
    # clicar no banner ativo > page de detalhamento do produto
    # pegar a disponibilidade
    # assert == "Out Of Stock"

    main = MainPage(driver)
    main.click_first_banner()

    expected_status = "Out Of Stock"

    product_detail = ProductPage(driver)
    status = product_detail.get_availability_status()

    assert status == expected_status

    sleep(4)

def test_check_reviews_after_scrolling(driver):
    # dar scroll na main page até o final
    # clicar no segundo produto da seção Under @99
    # clicar na aba de REVIEWS
    # assert para checar que não existem revisões para este produto

    BasePage(driver).scroll_all_page()
    
    main = MainPage(driver)
    main.click_second_under_99_product()

    product_detail = ProductPage(driver)
    product_detail.click_review_tab()

    expected_message = "There are no reviews for this product."

    message = product_detail.get_reviews_tab_message()

    assert message == expected_message

    sleep(5)

def test_buy_from_category(driver):
    main = MainPage(driver)
    main.click_category_menu()
    main.click_camera_submenu()

    products_by_category = ProductsByCategory(driver)
    products_by_category.click_on_product(28)

    product_detail = ProductPage(driver)
    product_detail.click_add_to_cart_button()
    product_detail.click_notification_view_cart_button()

    cart = CartPage(driver)
    cart.click_checkout_button()

    checkout = CheckoutPage(driver)
    checkout.click_guest_checkout_option()
    checkout.fill_personal_details("Diana", "Neves", "diana@neves.pt", "999888777")
    checkout.fill_billing_details("EQA", "Rua A", "99dir", "Maia", "4200", "Portugal", "Porto")
    checkout.click_terms()
    checkout.click_continue_button()

    confirmation = ConfirmationPage(driver)
    confirmation.click_confirm_order_button()

    expected_message = "Your order has been placed!"

    final = FinalPage(driver)
    message = final.get_message(expected_message)

    assert message == expected_message

    sleep(5)
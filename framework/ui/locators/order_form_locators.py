from selenium.webdriver.common.by import By

from configuration.config_parse import *

BASE_URL = MAIN_UI_URL  # os.getenv('TEST_FRAMEWORK_BASE_URL')


class OrderFormtLocators:
    continue_button = (By.XPATH, "//*[@id='checkout_page_container']/div[1]/a")
    email_address_input = (By.XPATH, "//*[@id='wpsc_checkout_form_9']")
    first_name_input = (By.XPATH, "//*[@id='wpsc_checkout_form_2']")
    last_name_input = (By.XPATH, "//*[@id='wpsc_checkout_form_3']")
    address_input = (By.XPATH, "//*[@id='wpsc_checkout_form_4']")
    city_input = (By.XPATH, "//*[@id='wpsc_checkout_form_5']")
    state_input = (By.XPATH, "//*[@id='wpsc_checkout_form_6']")
    country_dropdown = (By.XPATH, "//*[@id='wpsc_checkout_form_7']")
    phone_input = (By.XPATH, "//*[@id='wpsc_checkout_form_18']")
    purchase_button = (By.XPATH, "//*[@id='wpsc_shopping_cart_container']/form/div[4]/div/div/span/input")
    purchase_complete_message = (By.XPATH, "//p[contains(.,'Thank you, your purchase is pending')]")

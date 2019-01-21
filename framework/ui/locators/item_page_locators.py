from selenium.webdriver.common.by import By

from configuration.config_parse import *

BASE_URL = MAIN_UI_URL  # os.getenv('TEST_FRAMEWORK_BASE_URL')


class ItemPageLocators:
    add_to_cart_button = (By.XPATH, "//*[@id='single_product_page_container']//input[@type='submit']")
    alert_added_to_cart = (By.XPATH, "//*[@id='single_product_page_container']//div[@class='alert addtocart']/p")

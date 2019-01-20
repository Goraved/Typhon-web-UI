from selenium.webdriver.common.by import By

from configuration.config_parse import *

BASE_URL = MAIN_UI_URL  # os.getenv('TEST_FRAMEWORK_BASE_URL')


class QaToolsHomePageLocators:
    url = 'http://store.demoqa.com/'
    product_category_tab = (By.XPATH, "//*[@id='menu-item-33']/a")
    macbook_category_menu = (By.XPATH, "//*[@id='menu-item-39']/a")
    macbook_item_link = (By.XPATH, "//*[@id='default_products_page_container']//a[contains(.,'MacBook')]")
    go_to_cart = (By.XPATH, "//*[@id='header_cart']/a")

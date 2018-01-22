from selenium.webdriver.common.by import By
from configuration.config_parse import *

BASE_URL = MAIN_UI_URL  # os.getenv('TEST_FRAMEWORK_BASE_URL')


class GoogleSearchLocators:
    search_field = (By.XPATH, "//*[@id='lst-ib']")
    url = "https://www.google.com"
    gmail_icon = (By.XPATH,"//a[@class='gb_P'][contains(.,'Gmail')]")
    help_link = (By.XPATH,"//*[@id='initialView']/footer/ul/li[1]/a")

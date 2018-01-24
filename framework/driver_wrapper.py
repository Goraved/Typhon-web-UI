from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from configuration.config_parse import *


class Driver:
    @staticmethod
    def get_driver():
        driver = None
        operation_system = platform.system()
        arch = platform.architecture()
        if BROWSER == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif BROWSER == 'firefox':
            if operation_system == "Darwin" or "Linux":
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            else:
                if arch[0] == "32bit":
                    driver = webdriver.Firefox(executable_path=GeckoDriverManager(os_type="win32").install())
                elif arch[0] == "64bit":
                    driver = webdriver.Firefox(executable_path=GeckoDriverManager(os_type="win64").install())
        elif BROWSER == 'safari':
            driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        elif BROWSER == 'ie':
            if arch[0] == "32bit":
                driver = webdriver.Ie(executable_path=IEDriverManager(os_type="Win32").install())
            elif arch[0] == "64bit":
                driver = webdriver.Ie(executable_path=IEDriverManager(os_type="x64").install())
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1280, 1024)
        return driver

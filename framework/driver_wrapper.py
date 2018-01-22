import platform
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager import utils

from configuration.config_parse import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

BROWSERS = {
    "chrome": DesiredCapabilities.CHROME,
    "firefox": DesiredCapabilities.FIREFOX
}


class Driver:
    @staticmethod
    def get_driver():
        driver = None
        operation_system = platform.system()
        arch = platform.architecture()
        # if os.environ.get('SELENIUM_CONNECTION') == 'LOCAL':
        #     path = os.environ.get('SELENIUM_DRIVER_PATH')
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
        # # else:
        #     if os.environ.get('SELENIUM_CONNECTION') == 'REMOTE':
        #         driver = webdriver.Remote(
        #             command_executor=os.environ.get('SELENIUM_RC_URL'),
        #             desired_capabilities=BROWSERS[os.environ.get('SELENIUM_BROWSER')])
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(20)
        driver.set_window_size(1280, 1024)
        return driver

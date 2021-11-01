import os

import allure
import gevent
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver

from base_definitions import ROOT_DIR
from configuration.config_parse import GITHUB, OS_VERSION


class Utilities:
    @staticmethod
    def get_screenshot(driver: WebDriver):
        if not driver:
            return
        try:
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        except WebDriverException:
            pass  # Session timed out

    @staticmethod
    def get_html_source(driver: WebDriver):
        if not driver:
            return
        try:
            html = driver.page_source
            if html:
                allure.attach(html, name='html_source', attachment_type=allure.attachment_type.HTML)
            console_log = driver.get_log('browser')
            if console_log:
                console_text = '\n\n'.join([f'{_["level"]} - {_["message"]}' for _ in console_log])
                allure.attach(console_text, name='console_log', attachment_type=allure.attachment_type.TEXT)
        except WebDriverException:
            pass  # Session timed out

    @staticmethod
    def fix_properties(driver):
        browser = os.getenv('browser', 'chrome').upper()
        properties_path = f'{ROOT_DIR}/allure-results/environment.properties'
        if os.path.isdir(f"{ROOT_DIR}/allure-results"):
            if os.path.exists(properties_path):
                remove_cycles = 10
                wait_interval = 1
                for _ in range(remove_cycles):
                    try:
                        os.remove(properties_path)
                        break
                    except FileNotFoundError:
                        gevent.sleep(wait_interval)  # will be useful in parallel mode
        else:
            os.mkdir(f"{ROOT_DIR}/allure-results")
        with open(properties_path, "w+") as file:
            file.write(f"Environment {os.getenv('ENVIRONMENT', '').upper()}\n")
            file.write(f"Browser {browser}\n")
            try:
                file.write(f"{browser}_VERSION {driver.capabilities['browserVersion']}\n")
            except KeyError:
                file.write(f"{browser}_VERSION {driver.capabilities['version']}\n")
            file.write(f"Git {GITHUB}\n")
            file.write(f"OS_VERSION {OS_VERSION}\n")
            file.write(f"SELENIUM_VERSION {selenium.__version__}\n")
            file.write(f"HEADLESS {os.getenv('HEADLESS')}\n")

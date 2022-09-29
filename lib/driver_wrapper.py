import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from configuration.config_parse import IMPLICIT_SEC


class DriverManager:

    _driver = None

    @staticmethod
    def get_chrome_options():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("w3c", False)
        options.add_argument("--no-sandbox")
        return options

    @classmethod
    def set_driver(cls) -> WebDriver:
        driver = None
        browser = os.getenv("browser", "chrome")
        if os.getenv("GITHUB_RUN"):
            options = cls.get_chrome_options()
            capabilities = {"browserName": browser, "sessionTimeout": "5m"}
            capabilities.update(options.to_capabilities())
            driver = webdriver.Remote(
                command_executor=os.getenv("SELENIUM_HUB_HOST"),
                desired_capabilities=capabilities,
            )
            return cls.add_driver_settings(driver)
        if browser == "chrome":
            options = Options()
            if os.getenv("HEADLESS", "false").lower() == "true" or os.getenv(
                "DOCKER_RUN"
            ):
                options = cls.get_chrome_options()
            driver = webdriver.Chrome(
                ChromeDriverManager(version="105.0.5195.52").install(),
                options=options,
                desired_capabilities={"goog:loggingPrefs": {"performance": "ALL"}},
            )

        elif browser == "firefox":
            operation_system = platform.system()
            arch = platform.architecture()
            if operation_system in ("Darwin", "Linux"):
                driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install()
                )
            else:
                if arch[0] == "32bit":
                    driver = webdriver.Firefox(
                        executable_path=GeckoDriverManager(os_type="win32").install()
                    )
                elif arch[0] == "64bit":
                    driver = webdriver.Firefox(
                        executable_path=GeckoDriverManager(os_type="win64").install()
                    )
        elif browser == "safari":
            driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
        elif browser == "ie":
            arch = platform.architecture()
            if arch[0] == "32bit":
                driver = webdriver.Ie(
                    executable_path=IEDriverManager(os_type="Win32").install()
                )
            elif arch[0] == "64bit":
                driver = webdriver.Ie(
                    executable_path=IEDriverManager(os_type="x64").install()
                )
        cls._driver = cls.add_driver_settings(driver)
        return cls._driver

    @classmethod
    def get_driver(cls) -> WebDriver:
        return getattr(cls, "_driver", None) or cls.set_driver()

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(IMPLICIT_SEC)
        driver.set_page_load_timeout(30)
        driver.maximize_window()
        return driver

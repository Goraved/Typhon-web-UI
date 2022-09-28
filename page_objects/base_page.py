import json
import time
from datetime import datetime, timedelta

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from configuration.config_parse import MAIN_UI_URL
from lib.driver_wrapper import DriverManager


class BasePage:
    def __init__(self, base_url: str = MAIN_UI_URL):
        self.driver = DriverManager().get_driver()
        self.base_url = base_url

    @allure.step("Open page - {url}")
    def open(self, url: str = ""):
        url = self.base_url + url
        self.driver.get(url)

    @allure.step("Redirect by url - {url}")
    def go_to_exact_url(self, url: str = ""):
        self.driver.get(url)

    # Get title of HTML page
    @allure.step("Get page title")
    def get_title(self) -> str:
        return self.driver.title

    # Get current url of a page
    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_current_url_contains_text(self, text: str):
        for _ in range(5):
            if text in self.get_current_url():
                break
            time.sleep(1)

    # Close system alerts like "Are you sure you want to leave this page?"
    def close_alert(self):
        self.driver.switch_to.alert.accept()

    # -> NAVIGATION

    def exit_frame(self):
        self.driver.switch_to.default_content()

    # Scroll to the top of the page
    def scroll_page_up(self, count: int = 3):
        for _ in range(0, count):
            ActionChains(self.driver).key_down(Keys.PAGE_UP).key_up(
                Keys.PAGE_UP
            ).perform()

    # Scroll to the bottom of the page
    def scroll_page_down(self, count: int = 3):
        for _ in range(0, count):
            ActionChains(self.driver).key_down(Keys.PAGE_DOWN).key_up(
                Keys.PAGE_DOWN
            ).perform()

    # Focus recently opened tab
    def focus_active_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

    # -> LOGS
    def get_network_logs(
        self, event_type: str = "request", seconds: int = 10
    ) -> list[dict]:
        browser_log = self.driver.get_log("performance")
        events = [self.process_browser_log_entry(entry) for entry in browser_log]
        if event_type == "request":
            events = [
                event["params"].get(event_type)
                for event in events
                if f"Network.{event_type}" in event["method"]
                and datetime.fromtimestamp(event["params"].get("wallTime", 0))
                > (datetime.now() - timedelta(seconds=seconds))
            ]
        else:
            events = [
                event["params"].get(event_type)
                for event in events
                if f"Network.{event_type}" in event["method"]
            ]
        return events

    @staticmethod
    def process_browser_log_entry(entry):
        response = json.loads(entry["message"])["message"]
        return response

    def get_console_log(self) -> str:
        return "; \n".join([_["message"] for _ in self.driver.get_log("browser")])

import json
import os
import time
from datetime import datetime, timedelta
from typing import List

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException, \
    StaleElementReferenceException, WebDriverException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from configuration.config_parse import MAIN_UI_URL, TIMEOUT_SEC


class BasePage:
    timeout_sec = TIMEOUT_SEC

    def __init__(self, driver, base_url: str = MAIN_UI_URL):
        self.driver = driver
        self.base_url = base_url

    @allure.step('Open page - {url}')
    def open(self, url: str = ""):
        url = self.base_url + url
        self.driver.get(url)

    @allure.step('Redirect by url - {url}')
    def go_to_exact_url(self, url: str = ""):
        self.driver.get(url)

    # Find element on page
    def find_element(self, *locator: tuple, timeout: float = timeout_sec) -> WebElement:
        self.wait_until_element_is_present(locator, timeout)
        return self.driver.find_element(*locator)

    # Find array of elements on page (useful for table, lists, dropdowns etc.)
    def find_elements(self, *locator: tuple, timeout: float = timeout_sec, wait: bool = True) -> List[WebElement]:
        if wait:
            self.wait_until_element_is_present(locator, timeout)
        return self.driver.find_elements(*locator)

    # Click on web element
    @allure.step('Click on element - {locator}')
    def click(self, *locator: tuple, timeout: float = timeout_sec):
        self.wait_until_element_is_clickable(locator, timeout=timeout)
        # Regular click
        try:
            self.find_element(*locator).click()
        except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
            # Scroll if not able to click
            try:
                self.scroll_element_to_center_by_js(self.find_element(*locator))
                self.find_element(*locator).click()
            # Click with JS
            except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
                self.click_element_with_js(self.find_element(*locator))
        except NoSuchWindowException:
            self.exit_frame()
            self.find_element(*locator).click()

    # Hove on web element
    @allure.step('Hover on element - {locator}')
    def hover(self, *locator: tuple):
        self.wait_until_element_is_visible(locator)
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    @allure.step('Click last element - {locator}')
    def click_last_element(self, *locator: tuple, timeout: float = timeout_sec):
        self.wait_until_element_is_clickable(locator, timeout=timeout)
        try:
            self.find_elements(*locator)[-1].click()
        except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
            # Scroll if not able to click
            try:
                self.scroll_element_to_center_by_js(self.find_elements(*locator)[-1])
                self.find_elements(*locator)[-1].click()
            # Click with JS
            except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException):
                self.click_element_with_js(self.find_elements(*locator)[-1])

    def click_element_with_js(self, element: WebElement):
        self.driver.execute_script("arguments[0].click()", element)

    # Click on web element and check that another element appear
    def click_and_check(self, click_locator: tuple, check_locator: tuple, timeout: float = timeout_sec):
        self.click(*click_locator, timeout=timeout)
        for _ in range(3):
            try:
                self.wait_until_element_is_clickable(check_locator, timeout=timeout / 2)
                return
            except (TimeoutException, NoSuchElementException):
                self.click(*click_locator)
        raise NoSuchElementException(f'Element - "{check_locator}" did not appear after clicking "{click_locator}"')

    # Click on web element and check that element missed
    def click_and_wait_for_element_to_be_hidden(self, *locator: tuple, timeout: int = timeout_sec):
        self.click(*locator, timeout=timeout)
        for _ in range(3):
            try:
                self.wait_until_element_is_hidden(locator, timeout=timeout)
                return
            except (TimeoutException, NoSuchElementException):
                self.click(*locator)
        raise Exception(f'Element - "{locator}" did not missed after clicking')

    # Click on web element and check that element not clickable
    def click_and_wait_for_element_to_be_not_clickable(self, *locator: tuple, timeout: int = timeout_sec):
        self.click(*locator, timeout=timeout)
        for _ in range(3):
            try:
                self.wait_until_element_is_not_clickable(locator, timeout=timeout)
                return
            except (TimeoutException, NoSuchElementException):
                self.click(*locator)
        raise Exception(f'Element - "{locator}" did not missed after clicking')

    def click_and_wait_for_other_element_to_be_hidden(self, click_locator: tuple, check_locator: tuple,
                                                      timeout: int = timeout_sec):
        self.click(*click_locator, timeout=timeout)
        for _ in range(3):
            try:
                self.wait_until_element_is_hidden(check_locator, timeout=timeout)
                return
            except (TimeoutException, NoSuchElementException):
                self.click(*click_locator)
        raise Exception(f'Element - "{check_locator}" did not missed after clicking - "{click_locator}"')

    # Click on web element only if it's visible
    def click_if_element_visible(self, *locator: tuple, timeout: int = timeout_sec):
        if self.is_element_visible(*locator, timeout=timeout):
            self.click(*locator)

    def click_child_element(self, parent_element: WebElement, child_locator: tuple):
        try:
            child_element = WebDriverWait(parent_element, TIMEOUT_SEC).until(
                ec.element_to_be_clickable(child_locator)
            )
            self.scroll_element_to_center_by_js(child_element)
            child_element.click()
        except (ElementNotInteractableException, WebDriverException, TimeoutException) as exception:
            if type(exception) == WebDriverException and "is not clickable at point" not in str(exception):
                raise exception
            else:
                child_element = WebDriverWait(parent_element, TIMEOUT_SEC).until(
                    ec.visibility_of_element_located(child_locator)
                )
                self.scroll_element_to_center_by_js(child_element)
                self.driver.execute_script("arguments[0].click()", child_element)
                print("Clicked with JS. Element may not have been actually clicked")

    @allure.step('Type text "{text}" into element - {locator}')
    def type(self, text: str, *locator: tuple):
        self.wait_until_element_is_visible(locator)
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Type text "{text}" into element - {locator} without waiting and clearing')
    def type_without_clearing(self, text, locator):
        self.find_element(*locator).send_keys(text)

    @allure.step('Upload file "{filename}" into element - {locator}')
    def upload_file(self, filename: str, *locator: tuple):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(filename)

    # Clear text field of element
    def clear(self, *locator: tuple):
        element = self.find_element(*locator)
        element.clear()

    # Scroll to web element
    def move_to_element(self, *locator: tuple):
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Press TAB into element - {locator}')
    def defocus_element(self, *locator):
        self.find_element(*locator).send_keys(Keys.TAB)

    @allure.step('Drag element {source_element} to {destination_element}')
    def drag_element_to_element(self, source_element, destination_element):
        source = self.find_element(*source_element)
        dest = self.find_element(*destination_element)
        ActionChains(self.driver).drag_and_drop(source, dest).perform()

    # -> CHECKERS

    # Check that checkbox is selected
    def is_element_selected(self, *locator: tuple) -> bool:
        element = self.find_element(*locator)
        return element.is_selected()

    def is_checked_checkbox(self, *locator: tuple) -> bool:
        checkbox = self.find_element(*locator)
        return checkbox.get_attribute('checked') == "true"

    # Check that element is enabled
    def is_element_enabled(self, *locator: tuple, timeout: float = timeout_sec) -> bool:
        element = self.find_element(*locator, timeout=timeout)
        return element.is_enabled()

    # Check that web element is present on the page
    def is_element_present(self, *locator: tuple, timeout: float = timeout_sec) -> bool:
        try:
            self.wait_until_element_is_present(locator, timeout=timeout)
        except NoSuchElementException:
            return False
        return True

    # Check if element is invisible on the page
    def is_element_invisible(self, *locator: tuple, timeout: float = timeout_sec) -> bool:
        try:
            self.wait_until_invisibility_of_element_located(locator, timeout=timeout)
        except NoSuchElementException:
            return False
        return True

    # Check if element is visible on the page
    def is_element_visible(self, *locator: tuple, timeout: float = timeout_sec) -> bool:
        try:
            self.wait_until_element_is_visible(locator, timeout=timeout)
        except NoSuchElementException:
            return False
        return True

    # Check if pop up present
    def is_popup_present(self, locator: tuple, timeout: float = timeout_sec) -> bool:
        try:
            self.wait_until_element_is_present(locator, timeout)
        except TimeoutException:
            return False
        return True

        # Check if file downloaded and then remove all downloaded files

    def check_if_file_downloaded(self, *locator: tuple):
        path = os.path.expanduser('~/downloads')
        count_of_files = [f for f in os.listdir(path)
                          if os.path.isfile(os.path.join(path, f))]
        self.click(*locator)
        current_count = [f for f in os.listdir(path)
                         if os.path.isfile(os.path.join(path, f))]
        file_downloaded = False
        for _ in range(5):
            if len(current_count) == len(count_of_files):
                time.sleep(1)
                current_count = [f for f in os.listdir(path)
                                 if os.path.isfile(os.path.join(path, f))]
            else:
                file_downloaded = True
                current_count.remove('.DS_Store')
                current_count = [os.path.join(path, f) for f in current_count]
                current_count.sort(key=lambda x: os.path.getctime(x))
                latest = current_count[-1]
                os.remove(latest)
        return file_downloaded

    # GETTERS

    # Get title of HTML page
    @allure.step('Get page title')
    def get_title(self) -> str:
        return self.driver.title

    # Get current url of a page
    def get_current_url(self) -> str:
        return self.driver.current_url

    # Get text from web element
    @allure.step('Get text of element - {locator}')
    def get_text(self, *locator: tuple, wait: bool = True, timeout: float = timeout_sec) -> str:
        if wait:
            self.wait_until_element_is_visible(locator, timeout=timeout)
            return self.find_element(*locator, timeout=timeout).text
        # If you don't need to fail test on NoSuchElementException
        else:
            if self.is_element_visible(*locator, timeout=timeout):
                return self.find_element(*locator, timeout=timeout).text

    @allure.step('Get text of many elements - {locator}')
    def get_text_of_many_elements(self, *locator: tuple, wait: bool = True, timeout: float = timeout_sec) -> list:
        return [element.text for element in self.find_elements(*locator, timeout=timeout, wait=wait)]

    # Get attribute needed value from
    @allure.step('Get attribute "{attribute}" value of element - {locator}')
    def get_attribute_value(self, attribute: str, *locator: tuple, timeout: float = timeout_sec) -> str:
        return self.find_element(*locator, timeout=timeout).get_attribute(attribute)

    @staticmethod
    def get_parametrized_locator(locator, parameter):
        return locator[0], locator[1].format(*parameter)

    @allure.step('Get options in the dropdown with the lazy loading')
    def get_all_options_from_lazy_loading_select(self, options_locator: tuple, wait: bool = True) -> List[str]:
        # For animation
        time.sleep(1)
        options = []
        previous_options = []
        while True:
            visible_options = self.find_elements(*options_locator, wait=wait)
            # Get texts and remove duplicates
            texts = [option.text for option in visible_options if option.text]
            options += texts
            # To check that list is still scrollable
            if previous_options == visible_options:
                return list(set(options))
            previous_options = visible_options
            self.scroll_element_to_center_by_js(visible_options[-1])

    # WAITERS
    def wait_current_url_contains_text(self, text: str):
        for _ in range(5):
            if text in self.get_current_url():
                break
            time.sleep(1)

    def wait_until_element_is_present(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not present in DOM after {timeout} seconds')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.presence_of_element_located, until=True, timeout=timeout)

    def wait_until_element_is_hidden(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until_not(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" was present for too long. '
                                         f'It takes more than {timeout} sec to hide an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.presence_of_element_located, until=False, timeout=timeout)

    def wait_until_element_is_not_clickable(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until_not(ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" was present for too long. It takes more than {timeout} sec to hide an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.presence_of_element_located, until=False, timeout=timeout)

    def wait_until_element_is_visible(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not visible after {timeout} seconds')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.visibility_of_element_located, until=True, timeout=timeout)

    # Wait until element will be clickable on the page
    def wait_until_element_is_clickable(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" not clickable. It takes more than {timeout} sec to load an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.element_to_be_clickable, until=True, timeout=timeout)
        except StaleElementReferenceException:
            time.sleep(1)
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_until_invisibility_of_element_located(self, locator: tuple, timeout: float = timeout_sec):
        try:
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" present. It takes more than {timeout} sec to hide an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, ec.invisibility_of_element_located, until=True, timeout=timeout)

    def wait_until_element_is_disabled(self, *locator: tuple, timeout: int = timeout_sec):
        for _ in range(timeout):
            if self.is_element_enabled(*locator, timeout=1):
                time.sleep(1)
            else:
                return
        raise Exception(f'Element {locator} has not be disabled during {timeout} seconds')

    # Hit "ENTER" button on web element
    def press_enter(self, *locator: tuple):
        self.find_element(*locator).send_keys(Keys.ENTER)

    # Close system alerts like "Are you sure you want to leave this page?"
    def close_alert(self):
        self.driver.switch_to.alert.accept()

    # -> NAVIGATION

    def exit_frame(self):
        self.driver.switch_to.default_content()

    # Scroll to the top of the page
    def scroll_page_up(self, count: int = 3):
        for _ in range(0, count):
            ActionChains(self.driver).key_down(Keys.PAGE_UP).key_up(Keys.PAGE_UP).perform()

    # Scroll to the bottom of the page
    def scroll_page_down(self, count: int = 3):
        for _ in range(0, count):
            ActionChains(self.driver).key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()

    # Remove web element using JS
    def remove_web_item(self, *locator: tuple):
        element = self.find_element(*locator)
        self.driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

    # Focus recently opened tab
    def focus_active_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

    def scroll_element_to_center_by_js(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", element)
        # sleep is needed to let JS actually finish scrolling
        time.sleep(0.5)

    @allure.step('Scroll lazy loading selector to the top')
    def scroll_lazy_loading_selector_to_the_top(self, options_locator: tuple):
        previous_options = []
        while True:
            visible_options = self.find_elements(*options_locator)
            if previous_options and visible_options == previous_options:
                break
            else:
                previous_options = visible_options
                self.scroll_element_to_center_by_js(visible_options[0])

    @allure.step('Scroll lazy loading selector to the bottom')
    def scroll_lazy_loading_selector_to_the_bottom(self, options_locator: tuple):
        previous_options = []
        while True:
            visible_options = self.find_elements(*options_locator)
            if previous_options and visible_options == previous_options:
                break
            else:
                previous_options = visible_options
                self.scroll_element_to_center_by_js(visible_options[-1])

    # -> SELECT

    @allure.step('Select value "value" by value in selector - {locator}')
    def select_by_value(self, value, *locator):
        select = Select(self.find_element(*locator))
        select.select_by_value(value)

    @allure.step('Select value "text" by text in selector - {locator}')
    def select_by_text(self, text, *locator):
        select = Select(self.find_element(*locator))
        select.select_by_visible_text(text)

    @allure.step('Select value "index" by index in selector - {locator}')
    def select_by_index(self, index, *locator):
        select = Select(self.find_element(*locator))
        select.select_by_index(index)

    # avoid unstable NoSuchWindow exception
    def avoid_no_such_window(self, locator: tuple, statement, until: bool, timeout: float = timeout_sec):
        for _ in range(5):
            try:
                if until:
                    WebDriverWait(self.driver, timeout).until(statement(locator))
                else:
                    WebDriverWait(self.driver, timeout).until_not(statement(locator))
                break
            except NoSuchWindowException:
                time.sleep(2)
        else:
            raise NoSuchElementException

    # -> LOGS
    def get_network_logs(self, event_type: str = 'request', seconds: int = 10) -> List[dict]:
        browser_log = self.driver.get_log('performance')
        events = [self.process_browser_log_entry(entry) for entry in browser_log]
        if event_type == 'request':
            events = [event['params'].get(event_type) for event in events if
                      f'Network.{event_type}' in event['method']
                      and datetime.fromtimestamp(event['params'].get('wallTime', 0)) > (
                              datetime.now() - timedelta(seconds=seconds))]
        else:
            events = [event['params'].get(event_type) for event in events if
                      f'Network.{event_type}' in event['method']]
        return events

    @staticmethod
    def process_browser_log_entry(entry):
        response = json.loads(entry['message'])['message']
        return response

    def get_console_log(self) -> str:
        return '; \n'.join([_['message'] for _ in self.driver.get_log('browser')])

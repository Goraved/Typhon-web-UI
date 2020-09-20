import os
import time

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from configuration.config_parse import MAIN_UI_URL, TIMEOUT_SEC


class BasePage:

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
    def find_element(self, *locator: tuple):
        return self.driver.find_element(*locator)

    # Find array of elements on page (useful for table, lists, dropdowns etc.)
    def find_elements(self, *locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step('Click on element - {locator}')
    def click(self, *locator: tuple):
        self.wait_until_element_is_clickable(locator)
        self.find_element(*locator).click()

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

    # Check that checkbox is selected
    def is_selected(self, *locator: tuple):
        element = self.find_element(*locator)
        return element.is_selected()

    # Check that element is enabled
    def is_enabled(self, *locator: tuple):
        element = self.find_element(*locator)
        return element.is_enabled()

    @allure.step('Get page titile')
    def get_title(self):
        return self.driver.title

    # Get current url of a page
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Hover on element - {locator}')
    def hover(self, *locator: tuple):
        self.wait_until_element_is_visible(locator)
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # Check that web element is present on the page
    def is_element_present(self, *locator: tuple):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    # Check if element is invisible on the page
    def is_element_invisible(self, *locator: tuple):
        try:
            self.wait_until_invisibility_of_element_located(locator)
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    # Check if element is visible on the page
    def is_element_visible(self, *locator: tuple):
        try:
            self.wait_until_element_is_visible(locator)
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    # avoid unstable NoSuchWindow exception
    def avoid_no_such_window(self, locator: tuple, statement, until, timeout: int = TIMEOUT_SEC):
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

    # WAITERS
    def wait_until_element_is_present(self, locator: tuple, timeout: int = TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not present in DOM after {timeout} seconds')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, EC.presence_of_element_located, until=True, timeout=timeout)

    def wait_until_element_is_hidden(self, locator: tuple, timeout: int = TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" was present for too long. It takes more than {timeout} sec to hide an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, EC.presence_of_element_located, until=False, timeout=timeout)

    def wait_until_element_is_visible(self, locator: tuple, timeout: int = TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not visible after {timeout} seconds')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, EC.visibility_of_element_located, until=True, timeout=timeout)

    # Wait until element will be clickable on the page
    def wait_until_element_is_clickable(self, locator: tuple, timeout: int = TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" not clickable. It takes more than {timeout} sec to load an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, EC.element_to_be_clickable, until=True, timeout=timeout)
        except StaleElementReferenceException:
            time.sleep(1)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_invisibility_of_element_located(self, locator: tuple, timeout: int = TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f'Element "{locator}" present. It takes more than {timeout} sec to hide an element')
        except NoSuchWindowException:
            self.avoid_no_such_window(locator, EC.invisibility_of_element_located, until=True, timeout=timeout)

    @allure.step('Get text of element - {locator}')
    def get_text(self, *locator: tuple):
        if self.is_element_visible(*locator):
            element = self.find_element(*locator)
            return element.text

    # Hit "ENTER" button on web element
    def press_enter(self, *locator: tuple):
        self.find_element(*locator).send_keys(Keys.ENTER)

    # Close system alerts like "Are you sure you want to leave this page?"
    def close_alert(self):
        self.driver.switch_to.alert.accept()

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

    @staticmethod
    def get_parametrized_locator(locator, parameter):
        return locator[0], locator[1].format(*parameter)

    @allure.step('Drag element {source_element} to {destination_element}')
    def drag_element_to_element(self, source_element, destination_element):
        source = self.find_element(*source_element)
        dest = self.find_element(*destination_element)
        ActionChains(self.driver).drag_and_drop(source, dest).perform()

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

    @allure.step('Get attribute "{attribute}" value of element - {locator}')
    def get_attribute_value(self, attribute: str, *locator: tuple):
        element = self.find_element(*locator)
        return element.get_attribute(attribute)

    @allure.step('Press TAB into element - {locator}')
    def defocus_element(self, *locator):
        self.find_element(*locator).send_keys(Keys.TAB)

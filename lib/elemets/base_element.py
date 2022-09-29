from functools import cached_property

from configuration.config_parse import TIMEOUT_SEC
from lib.selenium_driver import Driver


class BaseElement:
    def __init__(self, locator: tuple):
        self.locator = locator

    @cached_property
    def driver(self) -> Driver:
        return Driver()

    @property
    def is_selected(self) -> bool:
        return self.driver.is_element_selected(*self.locator)

    @property
    def is_checked(self) -> bool:
        return self.driver.is_checked_checkbox(*self.locator)

    @property
    def is_enabled(self) -> bool:
        return self.driver.is_element_enabled(*self.locator)

    @property
    def is_present(self) -> bool:
        return self.driver.is_element_present(*self.locator)

    @property
    def is_invisible(self) -> bool:
        return self.driver.is_element_invisible(*self.locator)

    @property
    def is_visible(self) -> bool:
        return self.driver.is_element_visible(*self.locator)

    @property
    def text(self) -> str:
        return self.driver.get_text(*self.locator)

    @property
    def text_of_all(self) -> list[str]:
        return self.driver.get_text_of_many_elements(*self.locator)

    def click(self, timeout: float = TIMEOUT_SEC):
        self.driver.click(*self.locator, timeout=timeout)

    def hover(self):
        self.driver.hover(*self.locator)

    def click_last_element(self):
        self.driver.click_last_element(*self.locator)

    def click_element_with_js(self):
        self.driver.click_element_with_js()

    # Click on web element and check that another element appear
    def click_and_check(self, check_locator: tuple):
        self.driver.click_and_check(self.locator, check_locator)

    # Click on web element and check that element missed
    def click_and_wait_for_element_to_be_hidden(self):
        self.driver.click_and_wait_for_element_to_be_hidden(*self.locator)

    def click_and_wait_for_element_to_be_not_clickable(self):
        self.driver.click_and_wait_for_element_to_be_not_clickable(*self.locator)

    def click_and_wait_for_other_element_to_be_hidden(self, check_locator: tuple):
        self.driver.click_and_wait_for_other_element_to_be_hidden(
            self.locator, check_locator
        )

    def click_if_element_visible(self):
        self.driver.click_if_element_visible(*self.locator)

    def type(self, text: str):
        self.driver.type(text, *self.locator)

    def type_without_clearing(self, text: str):
        self.driver.type_without_clearing(text, self.locator)

    def upload_file(self, filename: str):
        self.driver.upload_file(filename, *self.locator)

    def clear(self):
        self.driver.clear(*self.locator)

    def defocus_element(self):
        self.driver.defocus_element(self.locator)

    def drag_element_to_element(self, destination_element: tuple):
        self.driver.drag_element_to_element(*self.locator, *destination_element)

    def get_attribute_value(self, attribute: str) -> str:
        return self.driver.get_attribute_value(attribute, *self.locator)

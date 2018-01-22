import pytest
from framework.locators import *
from framework.base_page import BasePage


class QaItemPage(BasePage):
    @pytest.allure.step('Add Macbook to the cart')
    def add_macbook_to_cart(self):
        self.click(*ItemPageLocators.add_to_cart_button)
        return self.is_element_present(*ItemPageLocators.alert_added_to_cart)
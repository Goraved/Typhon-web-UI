import allure

from framework.ui.base_page import BasePage
from framework.ui.locators.item_page_locators import ItemPageLocators


class QaItemPage(BasePage):
    @allure.step('Add Macbook to the cart')
    def add_macbook_to_cart(self):
        self.click(*ItemPageLocators.add_to_cart_button)
        return self.is_element_present(*ItemPageLocators.alert_added_to_cart)

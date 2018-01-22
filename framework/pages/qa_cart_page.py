import pytest
from framework.locators import *
from framework.base_page import BasePage


class QaCartPage(BasePage):
    @pytest.allure.step('Purchase all items in the cart')
    def purchase_item(self):
        self.click(*OrderFormtLocators.continue_button)
        self.type('email@email.email', *OrderFormtLocators.email_address_input)
        self.type('First name', *OrderFormtLocators.first_name_input)
        self.type('Last name', *OrderFormtLocators.last_name_input)
        self.type('Address', *OrderFormtLocators.address_input)
        self.type('City', *OrderFormtLocators.city_input)
        self.type('State', *OrderFormtLocators.state_input)
        self.select_by_value('UA', *OrderFormtLocators.country_dropdown)
        self.type('123', *OrderFormtLocators.phone_input)
        self.click(*OrderFormtLocators.purchase_button)
        return self.is_element_present(*OrderFormtLocators.purchase_complete_message)

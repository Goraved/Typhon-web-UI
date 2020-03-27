from framework.ui.pages.qa_item_page import *
from tests.UI.qa_tools import TestQaToolsBase


@allure.feature('QA Tools')
class TestQaTools(TestQaToolsBase):

    @allure.step('01 - Purchase MacBook')
    def test_01_purchase_macbook(self):
        with allure.step('Go to the home page'):
            self.qa_home_page.go_to_qa_homepage()
        self.qa_home_page.go_to_macbook_category()
        self.qa_home_page.go_to_macbook_page()
        assert self.qa_item_page.add_macbook_to_cart()
        self.qa_home_page.go_to_cart_page()
        assert self.qa_order_page.purchase_item()

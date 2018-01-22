from tests.UI.test_base import TestBase
from framework.pages.qa_cart_page import *
from framework.pages.qa_item_page import *
from framework.pages.qa_tools_home_page import *


@pytest.allure.feature('QA Tools')
class TestQaTools(TestBase):
    @classmethod
    def setUpClass(cls):
        super(TestQaTools, cls).setUpClass()
        cls.qa_home_page = QaToolsHomePage(cls.driver)
        cls.qa_item_page = QaItemPage(cls.driver)
        cls.qa_order_page = QaCartPage(cls.driver)

    @pytest.allure.step('01 - Purchase MacBook')
    def test_01_purchase_macbook(self):
        self.qa_home_page.go_to_qa_homepage()
        self.qa_home_page.go_to_macbook_category()
        self.qa_home_page.go_to_macbook_page()
        self.assertTrue(self.qa_item_page.add_macbook_to_cart())
        self.qa_home_page.go_to_cart_page()
        self.assertTrue(self.qa_order_page.purchase_item())

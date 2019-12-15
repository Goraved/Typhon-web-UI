import allure

from framework.ui.pages.qa_cart_page import QaCartPage
from framework.ui.pages.qa_item_page import QaItemPage
from framework.ui.pages.qa_tools_home_page import QaToolsHomePage
from tests.UI import TestBase


@allure.feature('QA Tools')
class TestQaToolsBase(TestBase):
    @classmethod
    def setup_class(cls):
        super(TestQaToolsBase, cls).setup_class()
        cls.qa_home_page = QaToolsHomePage(cls.driver)
        cls.qa_item_page = QaItemPage(cls.driver)
        cls.qa_order_page = QaCartPage(cls.driver)

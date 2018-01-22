from framework.pages.google_search_page import *
from tests.UI.test_base import TestBase


@pytest.allure.feature('Events')
class TestGoogle(TestBase):
    @classmethod
    def setUpClass(cls):
        super(TestGoogle, cls).setUpClass()
        cls.google_page = GoogleSearchPage(cls.driver)
        cls.google_page.go_to_google_page()

    @pytest.allure.story('Check google search')
    @pytest.allure.testcase('[link to test case]', name=TEST_CASE)
    @pytest.allure.link(MAIN_UI_URL + 'search?q=what+is+selenium&oq=what+is+selenium&aqs=chrome..69i57j69i59j0l4.3694j0j7&sourceid=chrome&ie=UTF-8', name='What is selenium?')
    def testCheckSearch(self):
        self.assertTrue(self.google_page.search_field_present())  # Check search field present
        self.google_page.search_text()  # Use search
        self.assertTrue(self.google_page.check_page_title_equal_search())  # Check search works correctly




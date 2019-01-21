import pytest
from framework.ui.base_page import BasePage
from framework.ui.locators.google_search_locators import GoogleSearchLocators


class GoogleSearchPage(BasePage):
    # Go to google search page
    @pytest.allure.step('Login')
    def go_to_google_page(self):
        self.go_to_exact_url(GoogleSearchLocators.url)

    # Check that search field present
    def search_field_present(self):
        return self.is_element_present(*GoogleSearchLocators.search_field)

    # Enter some text to search and run
    @pytest.allure.step('Search specific information in Google')
    def search_text(self):
        self.type("What is selenium?",*GoogleSearchLocators.search_field)
        self.press_enter(*GoogleSearchLocators.search_field)

    # Check that HTML title equal to search
    @pytest.allure.step('Getting search result title')
    def check_page_title_equal_search(self):
        return self.get_title()

import allure

from framework.ui.base_page import BasePage
from framework.ui.locators.home_page_locators import QaToolsHomePageLocators


class QaToolsHomePage(BasePage):
    # Go to google search page
    @allure.step('Go to home page')
    def go_to_qa_homepage(self):
        self.go_to_exact_url(QaToolsHomePageLocators.url)

    @allure.step('Go to MacBook category')
    def go_to_macbook_category(self):
        self.hover(*QaToolsHomePageLocators.product_category_tab)
        self.click(*QaToolsHomePageLocators.macbook_category_menu)

    @allure.step('Go to MacBook page')
    def go_to_macbook_page(self):
        self.click(*QaToolsHomePageLocators.macbook_item_link)

    @allure.step('Go to the cart page')
    def go_to_cart_page(self):
        self.click(*QaToolsHomePageLocators.go_to_cart)

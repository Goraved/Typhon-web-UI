from selenium.webdriver.common.by import By

from lib.elemets.base_element import BaseElement
from page_objects.base_page import BasePage


class ShopPage(BasePage):
    @property
    def t_shirt_category_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, 'li:nth-child(3) > a[title="T-shirts"]'))

    @property
    def item_name_lbl(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, '[itemprop="name"]'))

    @property
    def add_to_cart_btn(self) -> BaseElement:
        return BaseElement((By.XPATH, '//a/span[text()="Add to cart"]'))

    @property
    def proceed_to_checkout_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, '[title="Proceed to checkout"]'))

    @property
    def second_cart_step_btn(self) -> BaseElement:
        return BaseElement(
            (
                By.CSS_SELECTOR,
                "p > a.button.btn.btn-default.standard-checkout.button-medium",
            )
        )

    @property
    def terms_checkbox(self) -> BaseElement:
        return BaseElement((By.XPATH, '//div[@id="uniform-cgv"]'))

    @property
    def pay_with_bank_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, '[title="Pay by bank wire"]'))

    @property
    def confirm_order_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, "#cart_navigation > button"))

    @property
    def profile_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, '[title="View my customer account"]'))

    @property
    def orders_btn(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, '[title="Orders"]'))

    @property
    def order_row(self) -> BaseElement:
        return BaseElement((By.CSS_SELECTOR, "#order-list > tbody > tr"))

    def open_site(self):
        self.open()

    def open_t_shirt_category(self):
        self.t_shirt_category_btn.click()

    def add_item_to_cart_and_proceed(self):
        self.item_name_lbl.hover()
        self.add_to_cart_btn.click()
        self.proceed_to_checkout_btn.click()

    def go_to_the_second_cart_step(self):
        self.second_cart_step_btn.click()

    def finish_order_after_registration(self):
        BaseElement((By.CSS_SELECTOR, "#center_column > form > p > button")).click()
        self.terms_checkbox.click()
        BaseElement((By.CSS_SELECTOR, "#form > p > button")).click()
        self.pay_with_bank_btn.click()
        self.confirm_order_btn.click()

    def open_profile_order_page(self):
        self.profile_btn.click()
        self.orders_btn.click()

    def is_order_present(self) -> bool:
        return self.order_row.is_present

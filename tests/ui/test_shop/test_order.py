import os

import allure
import pytest
from allure_commons._allure import step

from tests.ui.test_shop import TestShopBase


@allure.feature('Order')
class TestOrder(TestShopBase):

    @allure.title('Order T-Shirt')
    def test_order_t_shirt(self):
        with step('Open site'):
            self.shop_page.open_site()
        with step('Open T-Shirt category'):
            self.shop_page.open_t_shirt_category()
        with step('Add item to cart and proceed'):
            self.shop_page.add_item_to_cart_and_proceed()
        with step("Go to the second cart step"):
            self.shop_page.go_to_the_second_cart_step()
        with step('Register new account'):
            self.registration_page.register_account()
        with step('Finish order after registration'):
            self.shop_page.finish_order_after_registration()
        with step('Open profile orders page'):
            self.shop_page.open_profile_order_page()
        with step('Check at least 1 order present'):
            assert self.shop_page.is_order_present(), 'Order missed'

    @allure.title('Negative to check attachments')
    @pytest.mark.skipif(os.getenv('GITHUB_RUN') is not None, reason='GitHub actions')
    def test_negative(self):
        with step('Open site'):
            self.shop_page.open_site()
        with step('Fail test'):
            assert False

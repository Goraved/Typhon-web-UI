import allure

from page_objects.registation.registration_object import RegistrationPage
from page_objects.shop.shop_object import ShopPage
from tests.ui import TestBase


@allure.feature('Shop')
class TestShopBase(TestBase):
    @classmethod
    def setup_class(cls):
        super(TestShopBase, cls).setup_class()
        cls.shop_page = ShopPage()
        cls.registration_page = RegistrationPage()

import pytest

from lib.driver_wrapper import Driver
from lib.utilities import Utilities


class TestBase:
    driver = None
    properties = False

    @classmethod
    def setup_class(cls):
        cls.driver = Driver().get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.fixture(autouse=True)
    def fail_screenshot(self, request):
        yield
        # request.node is an "item" because we use the default
        if request.node.session.testsfailed != 0:
            Utilities.get_screenshot(self.driver)
            Utilities.get_html_source(self.driver)
        if not self.properties:
            Utilities.fix_properties(self.driver)
            self.properties = True

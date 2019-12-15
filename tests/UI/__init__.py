import pytest

from framework.ui.driver_wrapper import Driver
from framework.utilities import *


class TestBase:
    driver = None
    properties = False

    @classmethod
    def setup_class(cls):
        cls.driver = Driver.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        gevent.sleep(2)

    @pytest.fixture(autouse=True)
    def fail_screenshot(self, request):
        yield
        # request.node is an "item" because we use the default
        if request.node.session.testsfailed != 0:
            Utilities.get_screenshot(self)
            Utilities.get_html_source(self)
        if not self.properties:
            Utilities.fix_properties(self)
            self.properties = True

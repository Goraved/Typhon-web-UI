from allure_commons._allure import step

from framework.api.base_api import BaseAPI
from framework.utilities import *


class TestBase:
    properties = False

    def setup(self):
        self.step = step  # just need to not remove importing
        self.base_url = MAIN_API_URL
        # self.access_token = login() # Only if need Authorization
        self.base_api = BaseAPI()
        self.utilities = Utilities()

        if not self.properties:
            self.utilities.fix_api_properties()
            self.properties = True

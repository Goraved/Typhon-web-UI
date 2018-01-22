import requests

from framework.pages.google_search_page import *
from tests.API.test_base import *


@pytest.allure.feature('API')
class TestApi(TestBase):
    # Put here fields, that should be present in output response
    needed_fields = ["access_token", "token_type", "expires_in", "refresh_token", "iLoginStatus"]
    # Put here header
    headers = dict(
        content_type='application/x-www-form-urlencoded'
    )
    # Put here body (if required)
    body = dict(
        username=DICTIONARY.get('admin_login'),
        password=DICTIONARY.get('admin_pass')
    )
    # Put here attributes that should be present in link
    attributes = dict(
        # put attributes, which should be added to link
    )

    @classmethod
    def setUpClass(cls):
        super(TestApi, cls).setUpClass()

    @pytest.allure.story('01 - Check API status')
    @pytest.allure.testcase('[link to test case]', name=TEST_CASE)
    @pytest.allure.link(MAIN_API_URL + '/users/login', name='[API name]')
    def test_01_status(self):
        url = MAIN_API_URL + '/users/login'
        TestBase.response = requests.post(url, self.body, headers=self.headers)
        self.assertTrue(TestBase.response.status_code == 200, 'Status is %s' % TestBase.response.status_code)

    @pytest.allure.story('02 - Check all fields present')
    @pytest.allure.testcase('[link to test case]', name=TEST_CASE)
    def test_02_all_fields_present(self):
        check_needed_fields = check_all_fields_present(self.needed_fields, TestBase.response)
        self.assertTrue(check_needed_fields is None, 'Next fields are missed: %s' % check_needed_fields)

    @pytest.allure.story('03 - Check all fields have correct formant')
    @pytest.allure.testcase('[link to test case]', name=TEST_CASE)
    def test_03_check_all_types(self):
        types = dict(
            access_token='str',
            token_type='str',
            refresh_token='int'
        )
        check_types_of_fields(types, TestBase.response)

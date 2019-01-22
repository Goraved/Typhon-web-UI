from tests.API.test_base import *


@allure.feature('Books API')
class TestBookApi(TestBase):
    url = MAIN_API_URL
    # Put here header
    headers = {
        # if needed
    }
    # Put here body (if required)
    body = {
        # if needed
    }
    # Put here attributes that should be present in link
    attributes = {
        # if needed
    }
    book_id = '9789000010134'

    @classmethod
    def setUpClass(cls):
        super(TestBookApi, cls).setUpClass()

    @allure.step('01 - Check API status')
    def test_01_status_is_200(self):
        with step('Get books response'):
            TestBase.response = requests.get(f'{self.url}{self.book_id}')
        with step('Check response is 200'):
            self.assertTrue(TestBase.response.status_code == 200,
                            'Status is {%s} instead of 200' % TestBase.response.status_code)

    @allure.step('02 - Check all fields present')
    def test_02_check_all_fields_present(self):
        # Put here fields, that should be present in output response
        needed_fields = ['ISBN', 'Title', 'Subtitle', 'Description', 'CoverThumb', 'LanguageCode', 'Subjects',
                         'Authors']
        with step('Collect all missed fields'):
            missed_fields = check_all_fields_present(needed_fields, TestBase.response)
        with step('Check all fields present'):
            self.assertTrue(missed_fields is None, 'Next fields are missed %s' % missed_fields)

    @allure.step('03 - Check all fields have correct format')
    def test_03_check_all_types(self):
        # Put here fields and their types, that should be present in output response
        types = {
            'ISBN': 'str',
            'Title': 'str',
            'Subtitle': 'str',
            'Description': 'str',
            'CoverThumb': 'str',
            'Subjects': 'list',
            'Authors': 'list'
        }
        with step('Collect wrong field types'):
            wrong_types = check_types_of_fields(types, TestBase.response)
        with step('Check all fields have correct type'):
            self.assertTrue(wrong_types is None, 'Wrong data types: %s' % wrong_types)

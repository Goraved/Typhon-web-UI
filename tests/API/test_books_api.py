from tests.API import *


@allure.feature('Books API')
class TestBookApi(TestBase):
    book_id = '9789000010134'

    @allure.step('01 - Check API status')
    def test_01_status_is_200(self):
        with step('Get books response'):
            response = self.base_api.get(f'{MAIN_API_URL}{self.book_id}')
        with step('Check response is 200'):
            assert response.status_code == 200, f'Status is {response.status_code} instead of 200'

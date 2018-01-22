import requests

from framework.pages.google_search_page import *
from tests.API.test_base import *


@pytest.allure.feature('API')
class TestApi(TestBase):
    access_token = None
    headers = None

    @classmethod
    def setUpClass(cls):
        super(TestApi, cls).setUpClass()
        cls.access_token = cls.access_token
        cls.headers = dict(
            accept='application/json',
            Authorization='Bearer %s' % cls.access_token
        )

    @pytest.allure.story('01 - Check API GET')
    def test_01_get(self):
        attributes = dict(
            sLogin=DICTIONARY.get('admin_login'),
            iRecipientId=381404504,
            sSessionId='xxx',
            iOffset=0,
            iLimit=50,
            sSort='sDate'
        )
        url = generate_request_link('/customers/crm/virtualcloset?', attributes)
        TestBase.response = requests.get(url, headers=self.headers)
        self.assertTrue(TestBase.response.status_code == 200, 'Status is %s' % TestBase.response.status_code)

    @pytest.allure.story('02 - Check API POST')
    def test_02_post(self):
        attributes = dict(
            sLogin=DICTIONARY.get('admin_login'),
            sSessionId='xxx'
        )
        body = dict(
            iType=50,
            sStatus=["0", "30"],
            tsStart="2017-10-02",
            tsEnd="2017-10-29",
            iLimit=25,
            iOffset=0,
            sSort="sLastName"
        )
        url = generate_request_link('/todos/search?', attributes)
        TestBase.response = requests.post(url, body, headers=self.headers)
        self.assertTrue(TestBase.response.status_code == 200, 'Status is %s' % TestBase.response.status_code)

    @pytest.allure.story('03 - Check API PUT')
    def test_03_put(self):
        attributes = dict(
            sLogin=DICTIONARY.get('admin_login'),
            sSessionId='xxx'
        )
        body = [
            {'sTodoId': '644317970',
             'sStatusId': '30',
             'sActionId': '10003'}
        ]
        url = generate_request_link('/todos/60?', attributes)
        TestBase.response = requests.put(url, json=body, headers=self.headers)
        self.assertTrue(TestBase.response.status_code == 200, 'Status is %s' % TestBase.response.status_code)

    @pytest.allure.story('04 - Check API DELETE')
    def test_04_delete(self):
        attributes = dict(
            sLogin=DICTIONARY.get('admin_login'),
            sSessionId='xxx'
        )
        url = generate_request_link('/customers/crm/clientprofile/148125361/relative/645466406?', attributes)
        TestBase.response = requests.delete(url,  headers=self.headers)
        self.assertTrue(TestBase.response.status_code == 200, 'Status is %s' % TestBase.response.status_code)
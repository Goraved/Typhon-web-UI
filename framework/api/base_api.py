import requests

from framework.utilities import *


class BaseAPI:
    def __init__(self):
        self.auth_token = ''
        self.default_header = {'Content-Type': 'application/vnd.api+json', 'Authorization': self.auth_token}
        self.log = Utilities.log

    def auth(self):
        url = MAIN_API_URL + '/users/login'
        data = dict(
            username=config.get('CREDENTIALS', 'admin_login'),
            password=config.get('CREDENTIALS', 'admin_pass')
        )
        content_type = 'application/x-www-form-urlencoded'
        response = requests.post(url, data, content_type)
        response_body = response.json()
        return response_body.get('access_token')

        # Get API url and attributes to generate request link

    def get(self, path, **kwargs):
        headers = kwargs.get('headers', self.default_header)
        self.log(f'Sent GET request with: \n  URL = {path} \n  Headers = {headers}', msg_type='REQUEST')
        response = requests.get(path, headers)
        self.log(f'Status = {response.status_code} \n Response = {response.content}', msg_type='RESPONSE')
        assert response.status_code == 200
        return response

    def post(self, path, body, **kwargs):
        headers = kwargs.get('headers', self.default_header)
        self.log(f'Sent POST request with: \n  URL = {path} \n  Headers = {headers} \n  Body = {body}',
                 msg_type='REQUEST')
        response = requests.post(path, data=body, headers=headers)
        self.log(f'Status = {response.status_code} \n Response = {response.content}', msg_type='RESPONSE')
        assert response.status_code == 200
        return response

    def put(self, path, body, **kwargs):
        headers = kwargs.get('headers', self.default_header)
        self.log(f'Sent PUT request with: \n  URL = {path} \n  Headers = {headers} \n  Body = {body}',
                 msg_type='REQUEST')
        response = requests.put(path, data=body, headers=headers)
        self.log(f'Status = {response.status_code} \n Response = {response.content}', msg_type='RESPONSE')
        assert response.status_code == 200
        return response

    def patch(self, path, body, **kwargs):
        headers = kwargs.get('headers', self.default_header)
        self.log(f'Sent PATCH request with: \n  URL = {path} \n  Headers = {headers} \n  Body = {body}',
                 msg_type='REQUEST')
        response = requests.patch(path, data=body, headers=headers)
        self.log(f'Status = {response.status_code} \n Response = {response.content}', msg_type='RESPONSE')
        assert response.status_code == 200
        return response

    def delete(self, path, **kwargs):
        headers = kwargs.get('headers', self.default_header)
        self.log(f'Sent DELETE request with: \n  URL = {path} \n  Headers = {headers}', msg_type='REQUEST')
        response = requests.delete(path, headers=headers)
        self.log(f'Status = {response.status_code} \n Response = {response.content}', msg_type='RESPONSE')
        assert response.status_code == 200
        return response

    @allure.step('Generating request link')
    def generate_request_link(self, url, attributes):
        return MAIN_API_URL + url + '&'.join(
            ['%s=%s' % (key, value) for (key, value) in attributes.items()])

    # Get value from response by needed field
    @allure.step('Get value by specific field')
    def get_value(self, field, response):
        values = response.json()
        return values.get(field)

    # Check that all mentioned fields present in response
    @allure.step('Check that all needed fields present')
    def check_all_fields_present(self, fields, response):
        response_values = response.json()
        missed_fields = []
        for field in fields:
            if not field in response_values:
                missed_fields.append(field)
        if len(missed_fields) is 0:
            missed_fields = None
        else:
            ', '.join(missed_fields)
        return missed_fields

    # Check that response ordered according to specific value
    # def check_ordering(order_by, response):

    # Check that all fields has needed types
    @allure.step('Check that all fields have correct format type')
    def check_types_of_fields(self, types, response):
        values = response.json()
        wrong_types = []
        for field_type in types:
            value = self.get_value(field_type, response)
            actual_type = str(type(value).__name__)
            expected_type = types.get(field_type)
            if actual_type != expected_type:
                wrong_types.append('%s is {%s} instead of {%s}' % (field_type, actual_type, expected_type))
        if len(wrong_types) is 0:
            wrong_types = None
        else:
            ', '.join(wrong_types)
        return wrong_types

    # Check that response has needed length limit
    # def check_limit_of_response(limit, response):

    # Login and sending access_token to all APIs

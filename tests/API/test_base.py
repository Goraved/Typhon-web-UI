import requests
import unittest

import gevent

from framework.dictionary import DICTIONARY
from framework.utilities import *


def login():
    url = MAIN_API_URL + '/users/login'
    data = dict(
        username=DICTIONARY.get('admin_login'),
        password=DICTIONARY.get('admin_pass')
    )
    content_type = 'application/x-www-form-urlencoded'
    response = requests.post(url, data, content_type)
    response_body = response.json()
    return response_body.get('access_token')


def fix_properties():
    try:
        os.remove(ROOT_DIR + "/allureReports/environment.properties")
    except FileNotFoundError:
        "nothing"
    except:
        gevent.sleep(5)
        os.remove(ROOT_DIR + "/allureReports/environment.properties")
    f = open(ROOT_DIR + "/allureReports/environment.properties", "w+")
    f.write("Environment %s\n" % ENVIRONEMENT.upper())
    f.write("URL %s\n" % MAIN_API_URL)
    f.write("GitLab %s\n" % GITLAB)
    f.write("OS_NAME %s\n" % OS_NAME)
    f.write("OS_VERSION %s\n" % OS_VERSION)
    f.write("OS_ARCHITECTURE %s\n" % OS_ARCHITECTURE[0])


# Get API url and attributes to generate request link
@pytest.allure.step('Generating request link')
def generate_request_link(url, attributes):
    return MAIN_API_URL + url + '&'.join(
        ['%s=%s' % (key, value) for (key, value) in attributes.items()])


# Get value from response by needed field
@pytest.allure.step('Get value by specific field')
def get_value(field, response):
    values = response.json()
    return values.get(field)


# Check that all mentioned fields present in response
@pytest.allure.step('Check that all needed fields present')
def check_all_fields_present(fields, response):
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
@pytest.allure.step('Check that all fields have correct format type')
def check_types_of_fields(types, response):
    values = response.json()
    wrong_types = []
    for field_type in types:
        value = get_value(field_type, response)
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


class TestBase(unittest.TestCase):
    properties = False

    @classmethod
    def setUpClass(cls):
        cls.base_url = MAIN_API_URL
        # cls.access_token = login() # Only if need Authorization
        cls.response = None

    def tearDown(self):
        if not self.properties:
            fix_properties()
            self.properties = True

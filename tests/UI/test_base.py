import unittest
from enum import Enum

import gevent
import selenium
from framework.driver_wrapper import Driver
from framework.utilities import *


class TestBase(unittest.TestCase):
    driver = None
    properties = False

    @classmethod
    def setUpClass(cls):
        base_url = MAIN_UI_URL
        cls.driver = Driver.get_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        gevent.sleep(2)

    def tearDown(self):
        if not self.properties:
            self.fix_properties()
            self.properties = True
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
            errors = len(result.errors)
            failures = len(result.failures)
            if errors or failures != 0:
                Utilities.get_screenshot(self)

    def fix_properties(self):
        try:
            os.remove(ROOT_DIR + "/allureReports/environment.properties")
        except FileNotFoundError:
            "nothing"
        except:
            gevent.sleep(5)
            os.remove(ROOT_DIR + "/allureReports/environment.properties")
        f = open(ROOT_DIR + "/allureReports/environment.properties", "w+")
        f.write("Environment %s\n" % ENVIRONEMENT.upper())
        f.write("URL %s\n" % MAIN_UI_URL)
        f.write("Browser %s\n" % BROWSER.upper())
        f.write(BROWSER.upper() + "_VERSION %s\n" % self.driver.capabilities['version'])
        f.write("GitLab %s\n" % GITLAB)
        f.write("OS_NAME %s\n" % OS_NAME)
        f.write("OS_VERSION %s\n" % OS_VERSION)
        f.write("OS_ARCHITECTURE %s\n" % OS_ARCHITECTURE[0])
        f.write("SELENIUM_VERSION %s\n" % selenium.__version__)

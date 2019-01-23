import datetime

import allure
import gevent

from configuration.config_parse import *


class Utilities:
    def get_screenshot(self):
        date = datetime.datetime.now().strftime(" %Y-%m-%d %H %M %S")
        test_method_name = self._testMethodName + date
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name='failure_screenshot',
                          attachment_type=allure.attachment_type.PNG)
            file = f"{ROOT_DIR}/screenshots/Exception %s.png" % test_method_name
            self.driver.save_screenshot(file)
        except:
            file = f"{ROOT_DIR}/screenshots/Exception %s.png" % test_method_name
            self.driver.save_screenshot(file)

    @staticmethod
    def fix_api_properties():
        try:
            os.remove(ROOT_DIR + "/allure_reports/environment.properties")
        except FileNotFoundError:
            "nothing"
        except:
            gevent.sleep(5)
            os.remove(ROOT_DIR + "/allure_reports/environment.properties")
        f = open(ROOT_DIR + "/allure_reports/environment.properties", "w+")
        f.write("Environment %s\n" % ENVIRONEMENT.upper())
        f.write("URL %s\n" % MAIN_API_URL)
        f.write("GitLab %s\n" % GITLAB)
        f.write("OS_NAME %s\n" % OS_NAME)
        f.write("OS_VERSION %s\n" % OS_VERSION)
        f.write("OS_ARCHITECTURE %s\n" % OS_ARCHITECTURE[0])

    @staticmethod
    def log(msg, msg_type='DEBUG'):
        """
        Method will write log message to the allure report int 'stdout' tab
        """
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'{current_time} - {msg_type}: \n {msg}\n-------')

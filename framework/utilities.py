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
            os.remove(f"{ROOT_DIR}/allure_reports/environment.properties")
        except FileNotFoundError:
            "nothing"
        except:
            gevent.sleep(5)
            os.remove(f"{ROOT_DIR}/allure_reports/environment.properties")
        f = open(f"{ROOT_DIR}/allure_reports/environment.properties", "w+")
        f.write(f"Environment {ENVIRONEMENT.upper()}\n")
        f.write(f"URL {MAIN_API_URL}\n")
        f.write(f"GitLab {GITLAB}\n")
        f.write(f"OS_NAME {OS_NAME}\n")
        f.write(f"OS_VERSION {OS_VERSION}\n")
        f.write(f"OS_ARCHITECTURE {OS_ARCHITECTURE[0]}\n")

    @staticmethod
    def log(msg, msg_type='DEBUG'):
        """
        Method will write log message to the allure report int 'stdout' tab
        """
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'{current_time} - {msg_type}: \n {msg}\n-------')

import datetime

import allure
import gevent
import selenium

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

    def get_html_source(self):
        try:
            allure.attach(self.driver.page_source, name='html_source', attachment_type=allure.attachment_type.HTML)
        except:
            pass  # Local without allure

    def fix_properties(self):
        properties_path = f'{ROOT_DIR}/allure-results/environment.properties'
        if os.path.isdir(f"{ROOT_DIR}/allure-results"):
            if os.path.exists(properties_path):
                remove_cycles = 10
                wait_interval = 1
                for _ in range(remove_cycles):
                    try:
                        os.remove(properties_path)
                        break
                    except FileNotFoundError:
                        gevent.sleep(wait_interval)  # will be useful in parallel mode
        else:
            os.mkdir(f"{ROOT_DIR}/allure-results")
        f = open(properties_path, "w+")
        f.write("Environment %s\n" % os.getenv('ENVIRONMENT', '').upper())
        f.write("Browser %s\n" % BROWSER.upper())
        try:
            f.write(BROWSER.upper() + "_VERSION %s\n" % self.driver.capabilities['browserVersion'])
        except KeyError:
            f.write(BROWSER.upper() + "_VERSION %s\n" % self.driver.capabilities['version'])
        f.write("Git %s\n" % GITHUB)
        f.write("OS_VERSION %s\n" % OS_VERSION)
        f.write("SELENIUM_VERSION %s\n" % selenium.__version__)
        f.write("HEADLESS %s\n" % os.getenv('HEADLESS'))

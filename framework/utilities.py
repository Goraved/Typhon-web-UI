import datetime
import shutil

import pytest
import smtplib
from email.mime.text import MIMEText
from base_definitions import ROOT_DIR
from configuration.config_parse import *


class Utilities():
    def get_screenshot(self):
        date = datetime.datetime.now().strftime(" %Y-%m-%d %H %M %S")
        test_method_name = self._testMethodName + date
        try:
            pytest.allure.attach(self.driver.get_screenshot_as_png(), name='failure_screenshot',
                                 attachment_type=pytest.allure.attachment_type.PNG)
            file = ROOT_DIR + "/screenshots/Exception %s.png" % test_method_name
            self.driver.save_screenshot(file)
        except:
            file = ROOT_DIR + "/screenshots/Exception %s.png" % test_method_name
            self.driver.save_screenshot(file)

    # def send_email_with_last_run(self):
    #     directory = ROOT_DIR+'/allureReports'
    #     latest_run = max(directory, key=os.path.getmtime)
    #     latest_run += '/generated-report'
    #     shutil.make_archive('Last_test_run'+datetime.datetime.now().strftime(" %Y-%m-%d %H %M %S"), 'zip', latest_run)
    #     s = smtplib.SMTP('smtp.gmail.com')
    #     s.set_debuglevel(1)
    #     msg = MIMEText("""body""")
    #     sender = EMAIL_SENDER
    #     recipients = EMAIL_RECIPIENTS
    #     msg['Subject'] = " ".join(PROJECT, ENVIRONEMENT, 'last test run')
    #     msg['From'] = EMAIL_FROM
    #     msg['To'] = ", ".join(EMAIL_RECIPIENTS)
    #     s.sendmail(sender, recipients, msg.as_string())

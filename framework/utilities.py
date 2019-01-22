import datetime

import allure
from allure import step
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

    # def send_email_with_last_run(self):
    #     directory = ROOT_DIR+'/allure_reports'
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

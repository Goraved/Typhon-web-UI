import platform
import shutil
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from base_definitions import *
from configuration.config_parse import EMAIL_SENDER, PROJECT, ENVIRONEMENT

operation_system = platform.system()
if operation_system == "Darwin" or "Linux":
    directory = ROOT_DIR + '/allureReports/archive'
else:
    directory = ROOT_DIR + '\allureReports\archive'

folders = [os.path.join(directory, d) for d in os.listdir(directory)]
try:
    folders.remove(directory + '/.DS_Store')
    folders.remove(directory + '/.gitignore')
except:
    """nothing"""
latest_run = max(folders, key=os.path.getmtime)

if operation_system == "Darwin" or "Linux":
    file_name = 'Last_test_run' + latest_run.replace(directory + "/", "_")
    latest_run += '/generated-report'
else:
    file_name = 'Last_test_run' + latest_run.replace(directory + "\\", "_")
    latest_run += '\generated-report'

shutil.make_archive(file_name, 'zip', latest_run)

fromaddr = "QA team " + EMAIL_SENDER
toaddr = EMAIL_SENDER

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = " ".join([PROJECT, ENVIRONEMENT, 'last test run'])

body = ("""
Hello!
This a latest test run on the %s environment of the project %s !
Please download attached file, replace ".txt" by ".zip" and extract the folder.
Then use command "Allure open (path to folder)" to open the Allure report!

Have a nice day!
QA team!
""" % (ENVIRONEMENT, PROJECT))
msg.attach(MIMEText(body, 'plain'))

attachment = open(file_name + ".zip", "rb")

part = MIMEBase('application', None)
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % file_name + ".txt")

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('EMAIL', 'PASS')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
os.remove(file_name + '.zip')

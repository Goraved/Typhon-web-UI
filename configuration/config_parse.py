import configparser
import platform

from base_definitions import *

config = configparser.ConfigParser()

ENVIRONEMENT = os.getenv('ENVIRONMENT', 'DEV')
config.readfp(open(f'{ROOT_DIR}/configuration/{ENVIRONEMENT}.ini'))

# Attachment files
VIDEOFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'video_file_path')"
AVIFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'avi_file_path')"
BMPFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'bmp_file_path')"
DOCFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'doc_file_path')"
DOCXFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'docx_file_path')"
GIFFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'gif_file_path')"
JPGFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'jpg_file_path')"
MKVFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'mkv_file_path')"
MOVFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'mov_file_path')"
MP3FILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'mp3_file_path')"
MP4FILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'mp4_file_path')"
MPGFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'mpg_file_path')"
PDFFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'pdf_file_path')"
PNGFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'png_file_path')"
PPTFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'ppt_file_path')"
PPTXFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'pptx_file_path')"
RARFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'rar_file_path')"
TXTFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'txt_file_path')"
WAVFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'wav_file_path')"
XLSFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'xls_file_path')"
XLSXFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'xlsx_file_path')"
ZIPFILEPATH = f"{ROOT_DIR}/config.get('ATTACHMENTS', 'zip_file_path')"

# Environment settings
MAIN_UI_URL = config.get('PATH', 'main_UI_url')
MAIN_API_URL = config.get('PATH', 'main_API_url')
OS_NAME = platform.system()
OS_VERSION = platform.version()
OS_ARCHITECTURE = platform.architecture()
BROWSER = os.getenv('BROWSER', 'chrome')
PROJECT = config.get('ENVIRONMENT', 'project')
VIDEOFOLDERPATH = f"{ROOT_DIR}/config.get('ENVIRONMENT', 'video_folder_path')"
LINK_TYPE_TEST_CASE = config.get('ENVIRONMENT', 'link_type_test_case')
LINK_TYPE_LINK = config.get('ENVIRONMENT', 'link_type_link')
TEST_CASE = config.get('ENVIRONMENT', 'test_case')
EMAIL_RECIPIENTS = ['[email recipient]']
GITLAB = config.get('ENVIRONMENT', 'git_lab')
EMAIL_FROM = f"{PROJECT} QA TEAM"
EMAIL_SENDER = '[email sender]'

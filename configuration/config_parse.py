import platform
import configparser
from base_definitions import *

config = configparser.ConfigParser()

ENVIRONEMENT = 'DEV'
if ENVIRONEMENT == 'DEV':
    config.readfp(open(ROOT_DIR + '/configuration/dev.ini'))
elif ENVIRONEMENT == 'STAGE':
    config.readfp(open(ROOT_DIR + '/configuration/stage.ini'))

# Attachment files
VIDEOFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'video_file_path')
AVIFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'avi_file_path')
BMPFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'bmp_file_path')
DOCFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'doc_file_path')
DOCXFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'docx_file_path')
GIFFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'gif_file_path')
JPGFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'jpg_file_path')
MKVFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'mkv_file_path')
MOVFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'mov_file_path')
MP3FILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'mp3_file_path')
MP4FILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'mp4_file_path')
MPGFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'mpg_file_path')
PDFFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'pdf_file_path')
PNGFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'png_file_path')
PPTFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'ppt_file_path')
PPTXFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'pptx_file_path')
RARFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'rar_file_path')
TXTFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'txt_file_path')
WAVFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'wav_file_path')
XLSFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'xls_file_path')
XLSXFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'xlsx_file_path')
ZIPFILEPATH = ROOT_DIR + config.get('ATTACHMENTS', 'zip_file_path')

# Environment settings
MAIN_UI_URL = config.get('PATH', 'main_UI_url')
MAIN_API_URL = config.get('PATH', 'main_API_url')
OS_NAME = platform.system()
OS_VERSION = platform.version()
OS_ARCHITECTURE = platform.architecture()
BROWSER = config.get('BROWSERS', 'browser')
PROJECT = config.get('ENVIRONMENT', 'project')
VIDEOFOLDERPATH = ROOT_DIR + config.get('ENVIRONMENT', 'video_folder_path')
LINK_TYPE_TEST_CASE = config.get('ENVIRONMENT', 'link_type_test_case')
LINK_TYPE_LINK = config.get('ENVIRONMENT', 'link_type_link')
TEST_CASE = config.get('ENVIRONMENT', 'test_case')
EMAIL_RECIPIENTS = ['[email recipient]']
GITLAB = config.get('ENVIRONMENT', 'git_lab')
EMAIL_FROM = PROJECT + " QA TEAM"
EMAIL_SENDER = '[email sender]'

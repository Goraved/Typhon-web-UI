import configparser
import platform

from base_definitions import *

env_config = configparser.ConfigParser()
ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEV')
env_config.read_file(open(f'{os.path.dirname(os.path.abspath(__file__))}/{ENVIRONMENT}.ini'))

global_config = configparser.ConfigParser()
global_config.read_file(open(f'{os.path.dirname(os.path.abspath(__file__))}/global.ini'))

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
MAIN_UI_URL = env_config.get('PATH', 'main_UI_url')
OS_NAME = platform.system()
OS_VERSION = platform.version()
OS_ARCHITECTURE = platform.architecture()
BROWSER = os.getenv('BROWSER', 'chrome')
PROJECT = global_config.get('ENVIRONMENT', 'project')
LINK_TYPE_TEST_CASE = global_config.get('ENVIRONMENT', 'link_type_test_case')
LINK_TYPE_LINK = global_config.get('ENVIRONMENT', 'link_type_link')
TEST_CASE = global_config.get('ENVIRONMENT', 'test_case')
BUG = global_config.get('ENVIRONMENT', 'bug')
GITHUB = global_config.get('ENVIRONMENT', 'github')

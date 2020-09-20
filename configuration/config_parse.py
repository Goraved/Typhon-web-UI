import os
import platform

import yaml

# All configs placed into config/configs.yaml file. Please declare only variables here and set all values in yaml file

CONFIGS = yaml.safe_load(open(f'{os.path.dirname(os.path.abspath(__file__))}/configs.yaml'))
ENV_CONFIGS = CONFIGS['environments'][os.getenv('ENVIRONMENT', 'dev')]
URLS = CONFIGS['urls']
GENERAL = CONFIGS['general']


def get_value(key: str, key_type: str, *args):
    """
    Get constant value from YAML file by default, or from environment variables if exists
    """
    value = os.getenv(key.upper(), key_type[key])
    if args and not os.getenv(key.upper()):
        value = value.format(*args)
    return value


# Environment settings
MAIN_UI_URL = get_value('main_ui_url', URLS)

PROJECT = get_value('project', GENERAL)
LINK_TYPE_TEST_CASE = get_value('link_type_test_case', GENERAL)
LINK_TYPE_LINK = get_value('link_type_link', GENERAL)
TEST_CASE = get_value('test_case', GENERAL)
BUG = get_value('bug', GENERAL)
GITHUB = get_value('git_path', GENERAL)

TIMEOUT_SEC = get_value('timeout_sec', CONFIGS)
IMPLICIT_SEC = get_value('implicit_sec', CONFIGS)

OS_NAME = platform.system()
OS_VERSION = platform.version()
OS_ARCHITECTURE = platform.architecture()
ATTACHMENTS_DIR = '/attachments'

# Attachments
VIDEO_FILE_PATH = f'{ATTACHMENTS_DIR}/SampleVideo_1280x720_2mb.mp4'
AVI_FILE_PATH = f'{ATTACHMENTS_DIR}/test.avi'
BMP_FILE_PATH = f'{ATTACHMENTS_DIR}/test.bmp'
DOC_FILE_PATH = f'{ATTACHMENTS_DIR}/test.doc'
DOCX_FILE_PATH = f'{ATTACHMENTS_DIR}/test.docx'
GIF_FILE_PATH = f'{ATTACHMENTS_DIR}/test.gif'
JPG_FILE_PATH = f'{ATTACHMENTS_DIR}/test.jpg'
MKV_FILE_PATH = f'{ATTACHMENTS_DIR}/test.mkv'
MOV_FILE_PATH = f'{ATTACHMENTS_DIR}/test.mov'
MP3_FILE_PATH = f'{ATTACHMENTS_DIR}/test.mp3'
MP4_FILE_PATH = f'{ATTACHMENTS_DIR}/test.mp4'
MPG_FILE_PATH = f'{ATTACHMENTS_DIR}/test.mpg'
PDF_FILE_PATH = f'{ATTACHMENTS_DIR}/test.pdf'
PNG_FILE_PATH = f'{ATTACHMENTS_DIR}/test.png'
PPT_FILE_PATH = f'{ATTACHMENTS_DIR}/test.ppt'
PPTX_FILE_PATH = f'{ATTACHMENTS_DIR}/test.pptx'
RAR_FILE_PATH = f'{ATTACHMENTS_DIR}/test.rar'
TXT_FILE_PATH = f'{ATTACHMENTS_DIR}/test.txt'
WAV_FILE_PATH = f'{ATTACHMENTS_DIR}/test.wav'
XLS_FILE_PATH = f'{ATTACHMENTS_DIR}/test.xls'
XLSX_FILE_PATH = f'{ATTACHMENTS_DIR}/test.xlsx'
ZIP_FILE_PATH = f'{ATTACHMENTS_DIR}/test.zip'

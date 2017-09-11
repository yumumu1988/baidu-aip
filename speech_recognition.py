from aip import AipSpeech
import os
import sys


APP_ID = '********'
API_KEY = '************************'
SECRET_KEY = '********************************'
TARGET_FILE = ''
SOURCE_PATH = ''


def get_api_object():
    return AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def append_to_file(results):
    with open(TARGET_FILE, 'a', encoding='UTF-8') as f:
        for r in results:
            f.write(r)
            f.write('\r\n')
            f.close()


def convert_voice(file_path, api_object):
    with open(file_path, 'rb') as fp:
        result = api_object.asr(fp.read(), 'wav', 16000, {'lan': 'zh'},)
        print('====%s====' % file_path)
        print(result)
        print('========')
        append_to_file(result.get('result', ['Empty']))


def unknown_fun(path):
    api_object = get_api_object()
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for f in sorted(files):
        convert_voice(f, api_object)


if __name__ == '__main__':
    if sys.argv[1] is None:
        print('No source path')
    else:
        if os.path.exists(sys.argv[1]):
            SOURCE_PATH = sys.argv[1]
            TARGET_FILE = os.path.join(SOURCE_PATH, r'target\meeting-record.txt')
            if not os.path.exists(os.path.join(SOURCE_PATH, 'target')):
                os.mkdir(os.path.join(SOURCE_PATH, 'target'))
            unknown_fun(SOURCE_PATH)
        else:
            print('Source path is invalid')

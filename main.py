from py_yandex import YaUploader


if __name__ == '__main__':
    TOKEN = ""

    uploader = YaUploader(TOKEN)
    result = uploader.upload('Test/test_.txt', 'test.txt')
    print(result)

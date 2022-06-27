import os
src = '/Users/logic/Desktop/pythoncode/file'
target = '/Users/logic/Desktop/pythoncode/fileCopy'


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        file_list = os.listdir(src)
        for i in file_list:
            path = os.path.join(src, i)
            with open(i, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target, i)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完毕!')


copy(src, target)


# import os
# # print(os.path)
# # path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
# # print(path)
# # print(type(path))
#
# with open('/Users/logic/Desktop/pythoncode/p1.jpg', 'rb') as stream:
#     container = stream.read()
#     print(stream.name)
#     file = stream.name
#
#     filename = file[file.rfind('\\') + 1:]
#     path = os.path.dirname(__file__)
#     path1 = os.path.join(path, filename)
#
#     with open(path1, 'wb') as wstream:
#         wstream.write(container)

import os
# address = os.path.abspath('a.txt')
# print(address)
#
# address = os.path.abspath(__file__)
# print(address)
#
# address = os.getcwd()  # 类似os.path.dirname(__file__)
# print(address)

path = '/Users/logic/Desktop/pythoncode/file/os01.py'
result = os.path.split(path)

print(result)  # 把文件和文件夹一刀割开
print(result[1])

# 扩展名：
result = os.path.splitext(path)
print(result)  # 扩展名

size = os.path.getsize(path)
print(size)

"""
os常用函数
dirname()
join()
split() 得到文件名
splittext() 得到文件扩展名
isabs()
isfile()
isdir()
"""

"""
os.path常用函数
import os
dir = os.getcwd()
打印文件夹目录


os.listdir() 返回指定目录下的所有的文件和文件夹
保存在列表里
"""

# 创建文件夹
# os.mkdir()

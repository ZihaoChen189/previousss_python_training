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

size = os.path.getsize(path)  # 文件大小
print(size)

os.path.join(os.getcwd(), 'file', 'a.txt')
"""
os常用函数
dirname()
join()拼接
split() 得到文件名
splittext() 得到文件扩展名
isabs()是绝对路径吗
isfile()是文件吗
isdir()是文件夹吗
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
# os.mkdir('目录')
# os.remove() 删除具体文件，给出具体路径
# os.rmdir() 如果存在文件，删除失败
# 用os.path.exists()判断文件夹里有没有文件

"""
删除一个存在文件的文件夹
"""
# path = '路径'
# file_list = os.listdir(path)
# for file in file_list:
#     # 得到的文件名字，但我们要完整的路径，需要拼接
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# else:
#     # 遍历完毕，删除目录
#     os.rmdir(path)
# print('删除成功')

# 切换目录
os.chdir('路径')

"""
os.getcwd()获取当前文件夹
os.listdir()浏览当前文件夹
os.mkdir()创建文件夹
os.remove() 删除一个文件
os.rmdir() 删除空的文件夹
"""



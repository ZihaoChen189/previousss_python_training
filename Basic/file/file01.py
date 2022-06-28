# a = open('a.txt', 'rt')
# container = a.read()
# print(container)
#
# result = a.readable()
# print(result)
#
# line = a.readline()  # 已经读过一遍了，你再搬管道里的东西，没有的
# print(line)

# while True:
#     line = a.readline()
#     print(line)
#     if not line:
#         break


# lines = a.readlines()  # 保存在列表中
# print(lines)
# for i in lines:
#     print(i)
#
# picture = open("p1.jpg", "rb")
# final = picture.read()
# print(final)

# a = open('a.txt', 'a')
# string = '欢迎来到系统'
# result = a.write(string)  # 每次都会将原来的内容清空，写当前的内容
# print(result)
# a.writelines(['你好呀\n', '欢迎您'])

# 用with,帮助我们自动释放资源
with open('a.txt', 'rb') as stream:
    container = stream.read()
    with open('b.txt', 'wb') as wstream:
        wstream.write(container)

print('文件复制完成')







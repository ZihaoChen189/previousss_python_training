# 可变参数

# 求和
# def get_sum(a, b):
#     r = a + b
#     print(r)


# get_sum(2, 6, 9)

# def get_sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     print("sum is:", s)
#
#
# ran_list = [1, 2, 3]
# get_sum(*ran_list)

# a, *b, c = 1, 2, 3, 4, 5
# print(a)
# print(b)
# print(c)

# 一个星星*：可以接受独立的变量
# 可变参数 两个星星**??????

# def show_book(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# show_book(bookname='西游记', author='吴承恩', number=5)
# show_book(bookname='西游记', author='吴承恩')
# show_book(bookname='西游记')
#
# book = {'bookname': '红楼梦', 'author': '曹雪芹'}
# show_book(**book)

def show_book(*args, **kwargs):
    print(args)  # 一个元祖
    print(kwargs)  # 一个字典


book = {'bookname': '坏小孩', 'author': 'zzz', 'number': 5}
show_book('龙少', '小芳', **book)


result = ".".join(["aa", "bb", "cc"])
print(result)
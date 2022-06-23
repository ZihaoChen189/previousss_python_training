islogin = False
def login(username, password):
    if username == 'admin' and password == '123':
        print('登录成功')
        global islogin
        islogin = True
    else:
        print('登录失败')


# def borrow_book(book_name):
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#     if login(username, password):
#         print('成功借阅{}'.format(book_name))
#     else:
#         print('未登录，不能借书')


def borrow_book(book_name):
    if islogin:
        print('成功借阅{}'.format(book_name))
    else:
        print('还没登录，不能借书')
        username = input('请输入用户名:')
        password = input('请输入密码:')
        login(username, password)


borrow_book('盗墓笔记')
borrow_book('盗墓')

# # 全局变量
# a = 100
#
#
# def test1():
#     # 局部变量
#     a = 0
#     b = 8
#     print("a=", a)
#     print("b=", b)
#
#
# def test2():
#     b = 9
#     print("a=", a)
#     # 有问题 print("b=", b)
#     print("b=", b)
#
#
# def test3():
#     global a
#     a -= 1
#     print("a=", a)
#
#
# test1()
# test2()
# test3()

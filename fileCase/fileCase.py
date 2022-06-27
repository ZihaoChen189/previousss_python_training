# 持久化保存: 文件
# 用户注册
def register():
    user_name = input("请输入用户名")
    password = input("请输入密码")
    repassword = input("请输入确认密码")
    if password == repassword:
        # 保存信息
        with open("/Users/logic/Desktop/pythoncode/fileCase/SQL/users.txt", "a") as write_stream:
            write_stream.write("{} {}\n".format(user_name, password))
        print("用户注册成功")
    else:
        print("密码不一样")


def login():
    user_name = input("请输入用户名")
    password = input("请输入密码")
    if user_name and password:
        with open("/Users/logic/Desktop/pythoncode/fileCase/SQL/users.txt") as read_stream:
            while True:
                user = read_stream.readline()
                if not user:
                    print("用户名或者密码有误")
                    break
                input_user = "{} {}\n".format(user_name, password)
                if user == input_user:
                    print("用户登录成功")
                    break


def showbooks():
    print("图书馆里面的书有：")
    with open("/Users/logic/Desktop/pythoncode/fileCase/SQL/书.txt") as read_stream:
        books = read_stream.readlines()
        for book in books:
            print(book, end='')


# 调用
# register()
# login()
showbooks()

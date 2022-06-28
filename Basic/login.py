def login(user, password):
    if user == 'admin' and password == '123456':
        print("登录成功")
    else:
        print("登录失败")


login("admin", "123456")

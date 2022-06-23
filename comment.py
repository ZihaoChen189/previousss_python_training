def login(username, password):
    """
    用户名登录
    :param username: 用户名
    :param password: 用户名密码
    :return: 是否登录成功
    """
    if username == 'admin' and password == '123':
        return True
    else:
        print('用户名或者密码有问题')
        return False


login()



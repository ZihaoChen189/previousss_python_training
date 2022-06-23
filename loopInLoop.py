def outer():
    a = 100

    def inner():
        b = 200
        # b += a  # 内部函数可以使用外部函数的变量
        # 如果在内部函数里，想修改外部函数的变量，用nonlocal
        nonlocal a
        a += b
        print('我是内部函数', b)
        print('我是内部函数', a)

    # result = locals()
    # print(result)
    print(a)
    inner()


outer()
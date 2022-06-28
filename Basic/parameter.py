def get_sum(a, b):
    print("函数", a, b)
    if isinstance(a, int) and isinstance(b, int):
        s = a + b
        print(s)
    else:
        print("类型错误")


get_sum("1", "5")

# 1 它是一个嵌套函数
# 2 内部函数引用了外部函数的变量
# 3 将内存函数返出，返回值是内部函数
def outer(n):
    a = 10

    def inner():
        b = a + n
        print('内部函数', b)
    return inner


r = outer(1)
print(r)

# 把内部函数扔出去

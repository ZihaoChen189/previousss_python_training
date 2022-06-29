number = 100
name = "陈紫灏"
__all__ = ["Calculate"]
# 放进去的，是可以用的，没放进去的，禁止使用


def add(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m += i
        return m
    else:
        print("至少两个参数！")
        return 0


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
    else:
        print("至少两个参数！")


def multiply(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m *= i
    else:
        print("至少两个参数！")


def test():
    print("test")


class Calculate:
    @classmethod
    def test1(cls):
        print("类方法")

    def __init__(self, num):
        self.num = num

    def test(self):
        print("正在使用计算器进行计算")


print(__name__)
if __name__ == "__main__":
    test()

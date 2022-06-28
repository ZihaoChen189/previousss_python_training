class Phone:
    # 魔术方法之一
    # 系统默认执行

    def __init__(self):  # 初始化init
        self.vara = 'abc'
        print("init")
    brand = '小米'
    price = 4999
    type = 'Mate 80'

    def call(self):
        print(self)
        print('正在打电话。。。。。')


phone1 = Phone()
# print(phone1.brand)
print(phone1)
phone1.call()

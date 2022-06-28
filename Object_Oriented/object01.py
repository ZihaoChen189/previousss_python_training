# 类 -> 对象 -> 属性 -> 方法
# 我们定义了一个类，默认继承了祖宗object类
class Phone(object):
    brand = 'HuaWei'


print(Phone)

# 使用类，创建对象
yp = Phone()
yp.brand = 'iPhone'
feifei = Phone()
print(yp.brand)
print(feifei.brand)

xiaowei = Phone()
print(xiaowei.brand)

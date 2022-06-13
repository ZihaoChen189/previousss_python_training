t1 = ()  # 元祖不能增加删除更改
print(type(t1))

t2 = ('aa')
print(type(t2))  # 这个暂时是一个字符串

t3 = ('aa',)
print(type(t3))  # 在后面加一个###逗号###，就是一个元祖了

# 根据设定的范围，来判断一个元祖中的元素位置
tx = ('a', 'b', 'c', 'd', 'e', 'a')

# index = tx.index('a', 1, 100)
# print(index)
#
# length = len(tx)
# print(length)
#
# for i in tx:
#     print(i)

tx = list(tx)
tx.append('add')
print(tx)

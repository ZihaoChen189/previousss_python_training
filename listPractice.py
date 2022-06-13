# # 增删改查
#
# list1 = []
# list2 = ['面包']
#
# list1.append('火腿肠')
#
# list1.append('辣条')
# print(list1)
#
# list2.append('薯条')
# print(list2)
#
# # list1 = list1 + list2
#
# list1.extend(list2)
#
# print(list1)

flag = True
container = []
while flag:

    name = input('商品名称:')
    price = input('商品价格:')
    number = input('商品数量:')

    goods = [name, price, number]

    container.append(goods)

    answer = input('是否继续添加(q/Q)')
    if answer.lower() == 'q':
        flag = False

# 遍历
for goods in container:
    print(goods)



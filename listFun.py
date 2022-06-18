# if 5 > 3:
#     print("---")
# else:
#     print("-")

# 列表推导式
# 1到20的数字
# list1 = []
# for i in range(1, 21):
#     list1.append(i)

list1 = [i for i in range(1, 21)]
list2 = [i + 2 for i in range(1, 10)]

print(list1)
print(list2)

list3 = [i for i in range(0, 100, 2)]
print(list3)

# ############### 如果有if判断？
list4 = [i for i in range(0, 101) if i % 2 == 0]
print(list4)

list5 = ['62', 'hello', '100', 'world', '88', 'luck']

list6 = [word for word in list5 if word.isalpha()]
list7 = [word.title() if word.startswith('h') else word.upper() for word in list5]
print(list6)
print(list7)

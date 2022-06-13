list = [5, 1, 7, 6, 8, 2, 4, 3]

for i in range(len(list) - 1):  # 轮数
    for j in range(0, len(list) - 1 - i):  # 两两比较
        if list[j] > list[j+1]:
            a = list[j]
            list[j] = list[j+1]
            list[j+1] = a
print(list)

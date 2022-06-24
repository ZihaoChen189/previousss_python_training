# 打印1～10 用递归

def test(i):
    if i == 10:
        print("10")
    else:
        print(i)
        i += 1
        test(i)


test(1)

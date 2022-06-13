# for i in range(10):  # 012。。9
#     print(i)
#
# for i in range(0,10):
#     print(i)

# for i in range(1, 11):  # 123。。10
#     print(i)

# for i in range(1, 11, 2):
#     print(i)
#
# for i in range(1, 11, 1):  # 第三个参数是步长step
#     print(i)
# r = 0
# for i in range(1, 51):
#     r += i
# print(r)


# 用了for else: for的循环走完，没被中断，则执行else里面的东西
# for i in range(3):
#     name = input('用户名')
#     password = input('密码')
#     if name == 'admin' and password == '12345':
#         print('用户登录成功!')
#         break
#     print('输入的东西不对劲啊')
# else:
#     print('账户被锁定！')
#
# n = 1
# while n < 10:
#     print(n)
#     n += 1
#     if n == 5:
#         break
# else:
#     print('over')

# 玩游戏要有金币，否则不能玩；玩游戏赠送一个金币，可以充值；充钱金额为10的倍数；玩一局消耗5个金币
# 猜大小：猜对了，给两个金币；猜错，没有奖励。没钱了，游戏结束，可以主动退出，没有金币主动退出
# 退出，打印金币数量是多少，超过6点以上就是大
# import random
# coinNumber = 0
# count = 0
#
# if coinNumber < 5:
#     print('金币不足，请充值')
#     money = int(input('请输入充值的金额，必须是10的倍数'))
#     while True:
#         if money % 10 == 0:
#             coinNumber += money // 10 * 20
#             print('当前金币有%d个' % coinNumber)
#             print('~~~~~游戏开始～～～～')
#             answer = input('是否开始游戏？Y/N？')
#
#             while coinNumber > 5 and answer == 'Y':
#                 coinNumber -= 5
#                 coinNumber += 1
#                 # 产生两个随机骰子数
#                 ran1 = random.randint(1, 6)
#                 ran2 = random.randint(1, 6)
#                 guess = input('请猜大小：')
#                 if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 <= 6:
#                     print('恭喜猜对！')
#                     # 奖励！
#                     coinNumber += 2
#                 else:
#                     print('猜错了！')
#                     coinNumber -= 1
#                 count += 1
#                 answer = input('继续游戏？Y/N?')
#             print('玩了%d次' % count)
#             break
#
#         else:
#             print('不是10的倍数，充值失败')


# for i in range(10):
#     if i % 3 != 0:
#         print(i)

# for i in range(10):
#     if i % 3 != 0:
#         continue
#     print(i)

n = 1
while n <= 5:
    m = 5
    while m >= n:
        print('*', end=' ')
        m -= 1
    n += 1
    print()




# a = 10
# b = 30
# if a > b:
#     c = a
# else:
#     c = b
# print('a和b两个数的较大值是%d' % c)
#
# a = 10
# b = 30
# c = a if a > b else b
# print('a和b两个数的较大值是%d' % c)  # if和else里面的代码少，才能这样省略
# print('aaaa') if a < b else print('bbbb')  # 赋值或者单纯的语句也可以
#
# # False:  0         ""   ''        None     ()  {}   []
# if 'hello':
#     print('1111')
# else:
#     print('else')

# n = 1
#
# while n <= 10:
#     print('-->n=%d' % n)
#     n += 1
#
# n = 1
# while n <= 50:
#     if n % 3 == 0:
#         print('---->', n)
#
#     n += 1
#
# n = 1
# sum = 0
# while n <= 10:
#     sum += n
#     n += 1
#
# print('累加和', sum)
#
# count = 0
# while True:
#     print('111')
#     count += 1
#     if count == 5:
#         break


# total = 0
# numbers = 0
# while True:
#
#     price = float(input('输入价格:'))
#     number = int(input('输入数量'))
#     total += price * number
#     numbers += number
#     answer = input('当前总额是：%.2f，是否添加商品？ Y/N' % total)
#     if answer == 'N':
#         break
#
# print('商品共%d 所有商品的总额是%.2f' % (numbers, total))
#
# import random
#
# value = random.randint(1, 50)
# count = 0
#
# while True:
#
#     guess = int(input('猜一个1～50的数字'))
#     count += 1
#     if guess == value:
#         if count == 1:
#             print('快去买彩票！')
#         elif 2 <= count <= 5:
#             print('运气还可以')
#         elif count >= 6:
#             print('运气一般！')
#         break
#     elif guess > value:
#         print('猜大了')
#     else:
#         print('猜小了')


import random
n = 1
personal_count = 0
machine_count = 0
while n <= 3:
    n += 1
    ran = random.randint(0, 2)
    guess = int(input('请输入剪刀0石头1布2\n'))
    if guess == 0 and ran == 2 or guess == 1 and ran == 0 or guess == 2 and ran == 1:
        print('我赢了！！！！！！！')
        personal_count += 1
    elif ran == 0 and guess == 2 or ran == 1 and guess == 0 or ran == 2 and guess == 1:
        print('机器赢了！！！！！')
    else:
        print('本轮平局！')
if personal_count > machine_count:
    print('我最终胜利！')
elif personal_count < machine_count:
    print('机器赢了！！')
else:
    print('平局！')

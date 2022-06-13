"""
1-5: 1000元
5-10: 笔记本
10-20: iphone12
超过了100: 特斯拉
else: 鼓励奖 毛绒玩具
"""
#
# money = 100000
# if 10000 < money <= 50000:
#     print("奖励1000元")
# elif 50000 < money <= 100000:
#     print("奖励一个笔记本电脑")
# elif 100000 < money <= 1000000:
#     print("iphone12")
# elif 1000000 > 1000000:
#     print("特斯拉")
# else:
#     print("毛绒玩具")


# print("----------人员管理系统---------")
# choice = input("请选择功能：1添加员工\n2删除员工\n3查询员工\n4修改员工信息\n")
#
# if choice == "1":
#     print("添加员工")
# elif choice == "2":
#     print("删除员工")
# elif choice == "3":
#     print("查询员工")
# elif choice == "4":
#     print("修改员工信息")
# else:
#     print("输入错误诶！")


# username = input("请输入用户名：")
# password = input("请输入密码：")
# is_remember = False
#
# if username == "admin" and password == "1234":
#     if is_remember:
#         print("已经记住了用户%s的密码了" % username)
#     else:
#         print("没有记住密码，需要下次输入")
#
# else:
#     print("用户名和密码有误")


print("----------shopping system-----------")
price = float(input("商品单价:"))
number = int(input("商品数量:"))
# 计算总额
total = price * number
# 选择付款方式
choice = input("请选择付款方式：1现金\n2微信\n3支付宝\n4刷卡")

if choice == "1":
    print("现金支付没有折扣，应付款金额为：%.2f" % total)
elif choice == "2":
    print("微信支付。。。")
    total *= 0.95
    print("应付款金额为：%.2f" % total)
elif choice == "3":
    total = total - total * 0.1
    print("支付宝支付。。。")
    print("应付款金额为：%.2f" % total)
elif choice == "4":
    print("刷卡支付。。。")
    if total > 100:
        total -= 20
        print("应付款金额为：%.2f" % total)
    else:
        print("没有折扣，应付款金额为：%.2f" % total)
else:
    print("输入有误！")





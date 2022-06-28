# # 替换内容
# s = '李泽："宝子，宝子来唱歌吧！"'
# result = s.replace('宝子', '**', 2)
# print(result)
#
# # 切割 右切割；左切割   split返回的是一个列表
# s = 'zihao jiayi cece'
# answe = s.split('e')
# answer = s.split(' ', 1)  # 只切一刀
# print(answe)
# print(answer)
#
# s = """好好学习！！！
# 好好学习！！！
# 好好学习！！！
# 好好学习！！！
# """
#
# result = s.splitlines()  # 按行分割
# print(result)
#
# test = 'zihao jiayi meizhu'
# result = test.partition(' ')  # 刀左面 + 参数 + 刀右面的
# print(result)
#
# string = 'hello world'
# result = string.title()
# print(result)
#
# result = string.upper()
# print(result)
#
# result = string.capitalize()
# print(result)
#
# username = input('用户名:')
# print(len(username))
#
# s = '        admin '
# result = s.strip()
# print(s)
# print(result)
#
# result = s.lstrip()
# print(result)
#
s = 'helloworld'
result = s.center(30)
print(result)

result = s.ljust(30)
print(result)

result = s.rjust(30)
print(result)
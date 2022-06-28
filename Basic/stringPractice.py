s1 = 'hello'
s2 = s1
s3 = 'hello'
s4 = 'hello1'

print(s1, s2, s3)
print(id(s1))
print(id(s2))
print(id(s3))

print(id(s4))

print(s1 is s4)

s1 = 'word'
print(s1, s2, s3)

s1 = 'ABCDEFG'

print(s1[4])
print(s1[-1], s1[6])

# 切片

s = 'ABCDEFG'

print(s[0:5])
print(s[-3:])

# 可以隔着取
print(s[::2])

print(s[::-1])
print(s[::-2])
# 字符串操作
# find从左到右，找不到相应的东西，返回-1
path = 'https://studentnet.cs.manchester.ac.uk/ugt/choices.php?programme=%23SPLUS4BB7C2&year=2021&currentyear=2021'
i = path.find('?')
name = path[i+1:]
print(i)
print(name)
# 从右面向左查找
i = path.rfind('?')
print(i)
dao = path[i:]
print(dao)

num = path.count('/')
print(num)
# index也可以查找，但是找不到会报错！

i = path.find('manches')
print(i)

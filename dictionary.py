dict = {}
print(type(dict))
dict['name'] = 'zihao'
dict['age'] = 20
dict['sex'] = 'male'
print(dict)

# key是无法修改的，只能修改value
dict['age'] = 21
print(dict)
# dict = {}
# print(type(dict))
# dict['name'] = 'zihao'
# dict['age'] = 20
# dict['sex'] = 'male'
# print(dict)
#
# # key是无法修改的，只能修改value
# dict['age'] = 21
# print(dict)

# book = {}
# book['书名'] = "《三体》"
# book['价格'] = 20
# book['作者'] = '刘慈欣'
# book['出版社'] = '***出版社'
# book['折扣'] = 0.8
#
# book['价格'] *= 0.8
#
#
# print(book)


book = {'书名': '《三体》', '价格': 16.0, '作者': '刘慈欣', '出版社': '***出版社', '折扣': 0.8}

# book.clear()
# 根据key进行删除, 删除的是键值对
# r = book.pop('出版社')
# print(r)
# print(book)

# r = book.popitem()  # 返回值是一个元组
# print(r)
# print(book)

# del book  # 都删除了
# print(book)

del book['价格']
print(book)
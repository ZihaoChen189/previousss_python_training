# # books = [ {'书名': '《三体》', '价格': 16, '作者': '刘慈欣', '出版社': '***出版社'},
# #                      {'书名': '《流浪地球》', '价格': 18, '作者': '刘慈欣', '出版社': '***出版社'} ]
# #
# # for book in books:
# #     book.pop('出版社')
# #
# # print(books)
#
# # 遍历 + 查询
#
# book = {'书名': '《三体》', '价格': 16.0, '作者': '刘慈欣'}
# # value = book.get('书名1', '默认')
# # # 第二个位置是一个default parameter 默认值
# # # get 根据key，得到对应的value数值
# # print(value)
#
# # print(len(book))
#
# # value = book['书名1']
# # print(value)
# # ###### 报错了
#
# # list = [1, 4, 7, 8, 9]
# # for i in list:
# #     print(i)
#
# # for i in book:
# #     print(i)
# # 取出来的是key 键值
# #
# # print(book.values())
# # for i in book.values():
# #     print(i)
#
# # book.values()  ; book.keys()
# # 如果想一对一对拿  =====> items()
#
# # for i in book.items():
# #     print(i)
# #
# # for k, v in book.items():
# #     print(k, v)
#
# # book.setdefault('出版社', '人民教育出版社')
# # # 只能增加， 不能更新，运行一次，还是第一次的信息
# # print(book)
#
# dict1 = {'a': 10, 'b': 20}
# # book.update(dict1)
# # print(book)  # 两个列表合并#####################
#
# # 两个字典之间不能用加号
#
# result = dict.fromkeys(['a', 'b'], 10)
# print(result)


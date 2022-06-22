# library = ['python精通', 'MySQL', '数据分析', '人工智能']
#
#
# def add_book(bookname):
#     library.append(bookname)
#     print("添加成功！")
#
#
# def show_book(books):
#     for book in books:
#         print(book)
#
#
# add_book('新概念英语')
# show_book(library)


list1 = [23, 45, 77, 80, 59, 10]


def get_list(list_1):
    # new_list = []
    # for e in list_1:
    #     if e >= 50:
    #         new_list.append(e)
    new_list = [e for e in list_1 if e >= 50]
    print(new_list)


get_list(list1)

def remove_from_list(list):
    # for e in list:
    #     if e <= 50:
    #         list.remove(e)
    # print(list)
    n = 0
    while n < len(list):
        if list[n] < 50:
            list.remove(list[n])
        else:
            n += 1
    print(list)

remove_from_list(list1)
print(list1)



msg = input('请发表一句话:')
print('~~~~~~~')
print('以下内容是回复内容:')
flag = True
while flag:
    name = input('请输入用户名:')
    while True:
        comment = input('输入评论:')
        comment = comment.strip()
        if len(comment) != 0:
            # 验证长度是否超出了20
            if len(comment) < 20:
                finalComment = comment.replace('丑陋', '**')
                print('{}发表的评论是:\n{}'.format(name, finalComment))
                flag = False
                break
            else:
                print('不能超出20个长度!')
        else:
            print('评论内容不能为空! ')



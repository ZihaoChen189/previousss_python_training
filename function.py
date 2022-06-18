import random


def generate_code(n):
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    code = ' '
    for i in range(n):
        r = random.choice(s)
        code += r
    print(code)
# print(generate_code)


generate_code(1000)

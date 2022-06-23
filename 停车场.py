import random
car_park = []


def enter():
    print('欢迎进入小郭的停车场')
    number = input('输入车牌号码:')
    car = {}
    car[number] = [0]
    car_park.append(car)
    print('{}已进场'.format(number))


def go_out():
    number = input('输入车牌号码:')
    for car in car_park:
        if number in car:
            time = random.randint(0, 24)
            time_record = car.get(number)
            time_record.append(time)
            cost = time * 4
            print('{}停车{}小时,应缴费{}元'.format(number, time, cost))
        else:
            print('此车未进场')


enter()
go_out()
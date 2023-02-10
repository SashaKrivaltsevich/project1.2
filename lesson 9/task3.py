"""
Написать функцию, которая принимает n-ое количество координат точек.
И в ответ возвращает длину маршрута между ними.
Каждая координата представлена кортежем, состоящим из двух объектов типа int.
"""
from math import sqrt


def common_length(f_point, s_point):
    res = sqrt((s_point[0] - f_point[0]) ** 2 + (s_point[1] - f_point[1]) ** 2)
    return res


def distance(*args):
    length = 0
    for index in range(len(args) - 1):
        length += common_length(args[index], args[index + 1])
    return length


result = distance((1, 1), (1, 2), (1, 3), (1, 1))
print(round(result, 5))

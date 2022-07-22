# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time


def find_num(x):
    a = str(time.time())
    b = ' '
    count = 1
    while count <= x:
        b += a[-count]
        count += 1
    return int(b)

print(find_num(3))
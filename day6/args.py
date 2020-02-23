"""
author:leolu
date:2020.02.23

函数
参数前加*代表是一个可变参数
可变参数：不确定参数个数

"""


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add(1))
print(add(1, 2, 3))
print(add(1, 34543, 656))

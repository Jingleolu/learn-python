"""
求最大公约数和最小公倍数
date:2020.03.01
author：leo

"""


def gys(x, y):
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            print("%d和%d的最大公约数是%d" % (x, y, i))
            break



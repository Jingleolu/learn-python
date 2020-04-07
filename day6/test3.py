"""
判断一个数是不是素数
date:2020-03-08
author:leolu
"""


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

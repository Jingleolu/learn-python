"""
判断输入的正整数是不是回文素数
利用之前的函数
date:2020-03-08
author:leolu
"""


import testhui as huiwen
import test3


if __name__ == '__main__':
    a = int(input('请输入一个数:'))
    if huiwen.is_palindrome(a) and test3.is_prime(a):
        print('%d是回文素数' % a)

"""
回文数：正反都能读通的数
author:leolu
date:2020.03.08

"""


def is_palindrome(num):
    num2 = num
    total = 0
    while num2 > 0:
        total = total * 10 + num % 10
        num2 //= 10
    answer = total == num
    return answer   # return total == num

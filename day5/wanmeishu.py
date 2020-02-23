"""
完美数
author:leolu
date:2019.02.10
完美数：三位数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
"""

import math
print('this is a program to print all wanmeishu whether your number is a prime number')
for x in range(2, 10000):
    end = int(math.sqrt(x))
    sum1 = 1
    for i in range(2, end + 1):
        if x % i == 0:
            sum1 += i + x / i
    if sum1 == x:
        print(x)

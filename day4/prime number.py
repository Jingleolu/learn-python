"""
author:jingleolu
date：2019.12.6
该程序为判断一个数是否为素数
判断过程为将一个数循环除从3到根号x的奇数

不过网上还有一个更高级的算法，叫筛法，具体百度
"""

import math
print('this is a program to judge whether your number is a prime number')
x = int(input('please input your number:'))
end = int(math.sqrt(x))
for i in range(2, end+1):
    if x % i != 0:
        continue
    else:
        print('%d不是素数' % x)
        break
print('%d是素数' % x)

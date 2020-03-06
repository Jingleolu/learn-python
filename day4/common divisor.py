"""
求两个数的最大公约数（最大公因数）
一个数能被两个数相乘得到，则称这两个数为因数(也就代表这个数除因数的余数为0）
那最大公约数就是这两个数分别各自相同有的最大因数
author：leolu
date：2019.12.08
"""
print('this is a programme caculate commom divisor')
a = int(input('please input your first number:'))
b = int(input('please input your second number:'))
if a > b:
    a, b = b, a
for divisor in range(a, 0, -1):
    if a % divisor == 0 and b % divisor == 0:
        print('%d和%d的公约数为%d' % (a, b, divisor))
        break
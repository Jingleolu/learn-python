"""
整数反转
author:leolu
date:2019.12.09
"""
num = int(input('please input the number you want to reverse:'))
reversed_num = 0
if num < 10:
    print('number is too small')
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

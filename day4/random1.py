"""
计算出一个1-100之间的随机数有人猜
"""

import random

final_number = random.randint(1, 100)
while True:
    a = int(input('输入要猜数字'))
    if a > final_number:
        print('大了')
    elif a < final_number:
        print('小了')
    else:
        print('猜对了')
        break

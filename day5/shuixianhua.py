"""
水仙花
author:leolu
date:2019.12.09
水仙花：三位数，个十百位的立方之和等于其本身
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

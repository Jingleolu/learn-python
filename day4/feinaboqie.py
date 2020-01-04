"""
author:leolu
date:2019.12.15
费那波切数列：斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，
每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
生成前20个数
"""
summary = 0
counter = 0
fab = [1, 0, 0]
for i in range(20):
    fab[2] = fab[0] + fab[1]
    fab[0] = fab[1]
    fab[1] = fab[2]
    summary = fab[2]
    counter = counter + 1
    print('第%d个数是%d' % (counter, summary))

"""
想的过于复杂
答案：
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
思路都是交换，但是直接一步到位
"""

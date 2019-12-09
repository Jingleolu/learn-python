"""
判断正整数是不是素数

"""


a = int(input('请输入一个正整数:'))
j = a - 1
if j > 0 and a % j == 0:
    print("%d是素数", a)
    else:
else:
    nums = j - 1
    while nums > 0 and a % nums != 0:
        nums -= nums
        print("%d是素数" % a)

"""
判断闰年
"""

print('this is a program to determin whether the year you put is leap'
      'year ')
year = int(input('please input the year: '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('是闰年')
else:
    print('不是闰年')

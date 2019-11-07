"""
英制与公制的厘米互换
"""


unit = str(input('请输入单位是厘米还是英寸:'))
data_part = float(input('please input your 长度:'))
if unit != '厘米' and unit != '英寸':
    print('单位错误')
elif unit == '厘米':
    print('转换成英寸的长度为:', data_part * 0.394)
else:
    print('转换成英寸的长度为:', data_part * 2.54)

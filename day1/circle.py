"""
根据半径计算周长和面积
"""
import math
r = float(input("please input circle's radius: "))

circle_length = 2 * math.pi * r
circle_area = math.pi * (r ** 2)
print('周长为:', circle_length)
print('面积为: %f' % circle_area)

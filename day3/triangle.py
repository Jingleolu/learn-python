"""
判断输入边长能否构成三角形，如果能则计算出三角形的周长和面积
"""

a, b, c = map(int, input('请输入三条边长:').split())
if a+b > c and a+c > b and b+c > a:
    print('三角形的周长为%d' % (a+b+c))
else:
    print('不能组成三角形')
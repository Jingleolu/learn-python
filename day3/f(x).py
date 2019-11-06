"""
分段求值
        3x-5 (x>1)
f(x)=   x+2 (-1<=x<=1)
        5x+3 (x<-1)
"""

x = float(input('x='))
if x is None:
    print('请输入数值')
else:
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(x)等于', y)

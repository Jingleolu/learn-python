"""
九九乘法表
"""
value = 0
for i in range(1, 10):
    for b in range(1, 10):
        value = i * b
        print('%dx%d=%d' % (i, b, value), end='\t')
    print()


'第二种写法（展现的表格式不一样）'
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

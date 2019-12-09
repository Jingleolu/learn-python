"""'
author:leolu
date:2019.12.9
打印三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'"""

print('this is a programme show different triangle')
print('first triangle')
row = int(input('please input your row number:'))
for i in range(1, row + 1):
    for j in range(0, i):
        print('*', end='')
    print()

print()
print('second triangle')

for i in range(1, row + 1):
    for j in range(row, 0, -1):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

print()
print('third triangle')

for i in range(0, row):
    for j in range(0, row * 2):
        if j < row - i or j > row + i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
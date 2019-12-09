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
for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()

print()
print('second triangle')

for i in range(1, 6):
    for j in range(5, 0, -1):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
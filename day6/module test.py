"""

from module1 import foo
foo()

from module2 import foo
foo()
"""

import module1
import module2 as m2
import module3
import test1

m2.foo()
module1.foo()
x = int(input("输入最大求公约数‘x'："))
y = int(input("输入'y'"))
test1.gys(x, y)

"""
from module2 import foo
from module1 import foo

最终输出hello world
被覆盖了
"""


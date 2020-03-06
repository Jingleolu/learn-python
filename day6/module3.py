def foo():
    print('this is foo')


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字（比如在别的test.py导入时，_name_就是test）
# 只有被Python解释器直接执行的模块的名字才是__main__
"""
如果有直接执行的代码，
"""
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
print("call leo")

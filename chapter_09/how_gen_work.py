# -*- coding: utf-8 -*-
import dis
import inspect

"""
    生成器的工作原理
"""

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()

# Python.exe 会调用一个叫做 PyEval_EvalFramEx(c函数) 去执行 foo函数，首先会创建一个栈帧
# Python 的代码是运行在C语言之上的


"""
Python 一切节对象，栈帧对象，字节码对象
当 foo 调用子涵数 bar ,又会创建一个栈帧
所有的栈帧都是分配在堆内存上，这几决定了栈帧可以独立于调用者存在
"""


def gen_func():
    yield 1
    name = "Tom"
    yield 2
    age = 20
    return "OK"


if __name__ == '__main__':

    # print(dis.dis(foo))

    foo()
    print(frame.f_code.co_name)
    caller_frame = frame.f_back
    print(caller_frame.f_code.co_name)

    gen = gen_func()
    print(dis.dis(gen))
    print('************************')

    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)



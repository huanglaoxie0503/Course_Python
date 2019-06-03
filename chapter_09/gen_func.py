# -*- coding: utf-8 -*-
"""
    生成器函数：
        函数里只要有关键字 yield 就是生成器函数
"""


def gen_func():
    yield 1
    yield 2
    yield 3


def func():
    return 1

# 生成器对象为惰性求值，延迟取值提供了可能
# 斐波拉契  0 1 1 2 3 5 8 ...


def fib(index):
    # 斐波拉契 方法一
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    # 斐波拉契 方法二
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list


def gen_fib(index):
    # 生成器实现斐波拉契 方法三
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


if __name__ == '__main__':
    # 返回生成器对象, 在 Python 编译字节码的时候就产生了
    gen = gen_func()

    for value in gen:
        print(value)

    result = func()

    info_01 = fib(10)
    print(info_01)

    info_02 = fib2(10)
    print(info_02)

    for data in gen_fib(100):
        print(data)

# -*- coding: utf-8 -*-
"""
    生成器函数：
        函数里只要有关键字 yield 就是生成器函数
"""


def gen_func():
    yield 1


def func():
    return 1


if __name__ == '__main__':
    gen = gen_func()

    re = func()

    pass

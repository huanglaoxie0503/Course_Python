# -*- coding: utf-8 -*-
from itertools import chain

"""
Python3.3 新加 yield from 语法
"""

my_list = [1, 2, 3]
my_dict = {
    "Tom1": "http://kuaixun.stcn.com/index_01.shtml",
    "Tom2": "http://kuaixun.stcn.com/index_02.shtml",
}


def gen_01(iterable):
    yield iterable


def gen_02(iterable):
    yield from iterable


def my_chain_01(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value


def my_chain_02(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


def gen_03(gen):
    yield from gen


def main():
    g = gen_03()
    g.send(None)

# mian 是调用方，gen_03 是委托生成器，gen 是子生成器
# yield from 会在调用方与子生成器之间建立一个双向通道


if __name__ == '__main__':
    # 1.
    for value in my_chain_01(my_list, my_dict, range(5, 10)):
        print(value)

    for value in my_chain_02(my_list, my_dict, range(5, 10)):
        print(value)

    # 2.
    for value in gen_01(range(10)):
        print(value)

    for value in gen_02(range(10)):
        print(value)

# -*- coding: utf-8 -*-
from threading import Thread

"""
    描述：
        super 函数
"""


class AA:
    def __init__(self):
        print("A")


class BB(AA):
    def __init__(self):
        print("B")
        super().__init__()


"""
    1. 既然重写了B的构造函数，为什么还要去调用super?
        MyThread 里 self.name = name 可以用 super().__init__(name=name) 代替
    2. super 到执行顺序是什么样的?
        执行 mro 顺序的上一级
"""


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        # self.name = name
        super().__init__(name=name)


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == '__main__':
    d = D()
    print(D.__mro__)

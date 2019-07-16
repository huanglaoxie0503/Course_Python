# -*- coding: utf-8 -*-
"""
    1.区别：
        __new__: 可以自定义类的生成过程，用来控制对象的生成过程，在对象生成之前
        __init__: __new__ 方法生成对象之后，对这个对象可以做操作，用来完善对象的
    2.__new__ 在 __init__ 之前调用
    3.如果 __new__ 方法不返回对象，则不会调用 __init__ 函数
"""


class User(object):
    def __new__(cls, *args, **kwargs):
        """
            可以自定义类的生成过程，可以在生成 User 对象之前加逻辑
        """
        print("in __new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("in __init__")
        self.name = name


if __name__ == '__main__':
    user = User(name="Tom")

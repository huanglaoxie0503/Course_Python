# -*- coding: utf-8 -*-
"""
    1. 什么是元类？
        元类就是创建类的类
            对象 < class(对象) < type

    2. 如何自定义元类？

    3. 类也是对象，type 是创建类的类

    4. Python 中类的实例化过程？
        首先寻找 metaclass ，通过 metaclass 去创建类(User)
"""


def create_class(name):
    if name == "user":
        class User(object):
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company(object):
            def __str__(self):
                return "company"
        return Company


"""
type 动态创建类、方法
"""
# User = type("user", (), {})


def say(self):
    # return self.name
    return "i am user"


class BaseClass(object):
    def answer(self):
        return "i am base_class"


class MetaClass(type):
    # 类也是对象，type 创建类的类
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    # User = type("user", (BaseClass, ), {"name": "user", "say": say})
    my_obj = User("Tom")
    print(my_obj)





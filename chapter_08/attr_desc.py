# -*- coding: utf-8 -*-
import numbers

"""
    描述：
        属性描述符：
            1. 数据属性描述性符
            2. 非数据属性描述符
        他们俩的属性查找顺序不一样
"""


class IntField(object):
    """
        1. 任何类，只要实现以下任何一个方法，就是属性描述符
        2. 数据属性描述符
    """
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 参数类型检查
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NoneDataIntField(object):
    """
        1. 非数据属性描述符
    """
    def __get__(self, instance, owner):
        pass


class Model(object):
    # age 是属性描述符的对象
    # age = IntField()
    age = NoneDataIntField()


if __name__ == '__main__':
    model = Model()
    model.age = 10
    print(getattr(model, "age"))
    print(model.__dict__)
    print(model.age)

    model.__dict__['age'] = "abc"
    print(model.__dict__)
    print(model.age)
    # user = User('Tom', date(year=1992, month=5, day=31))
    # print("in {0} file".format(__file__))
    #
    # res = user.get_age()
    # print(res)
    #
    # res_01 = user.age
    # print(res_01)
    #
    # user.age = 20
    # print(user._age)
    # print(user.age)

'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User(类)或其基类的__dict__中， 且age是data descriptor(数据描述符)， 那么调用其__get__方法, 否则

（2）如果“age”出现在user(对象)的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中

    （3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
    
    （3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError

'''



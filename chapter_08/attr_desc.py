# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 23:21
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




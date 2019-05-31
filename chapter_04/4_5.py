# -*- coding: utf-8 -*-

"""
    描述：
        Python 中类属性和实例属性以及查找顺序

        查找顺序是由下而上，先查找实例属性，再查找类属性，如果实例属性存在，则输出实例属性，否则继续往上查找类属性

        属性查找算法（多继承）：
            MRO算法 （深度优先，先左后右）
            BFS算法 （广度优先）
"""


class A:
    # 类属性
    name = "A"

    def __init__(self):
        # 实例属性
        self.name = "obj"


class D:
    pass


class C(D):
    pass


class B(D):
    pass


class E(B, C):
    pass


if __name__ == '__main__':
    a = A()
    # 查找顺序是由下而上，先查找实例属性，再查找类属性，如果实例属性存在，则输出实例属性，否则继续往上查找类属性
    result = a.name
    print(result)

    # 查找顺序：(<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
    # 菱形继承
    res = E.__mro__
    print(res)

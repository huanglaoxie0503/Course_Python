# -*- coding: utf-8 -*-

"""
    描述：
            Python 中的类变量和对象变量(实例的变量)
"""


class A:
    # 类变量
    aa = 1

    def __init__(self, x, y):
        """
            构造函数
        """
        self.x = x
        self.y = y


if __name__ == '__main__':
    # a = A(2, 3)
    # print(a.x, a.y, a.aa)
    # print(A.aa)

    # a = A(2, 3)
    # A.aa = 11
    # print(a.x, a.y, a.aa)
    # print(A.aa)

    a = A(2, 3)
    A.aa = 11
    # 本质上是在a对象上新建一个变量self.aa = aa
    a.aa = 100
    print(a.x, a.y, a.aa)
    print(A.aa)

    b = A(3, 5)
    print(b.aa)

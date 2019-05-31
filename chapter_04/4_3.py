# -*- coding: utf-8 -*-

"""
    描述：
        instance 和 type 的区别
"""


class A:
    pass


class B(A):
    pass


if __name__ == '__main__':
    b = B()
    judge_1 = isinstance(b, B)
    print(judge_1)

    judge_2 = isinstance(b, A)
    print(judge_2)

    judge_3 = type(b)
    """ is 和 == 符号不一样，不可乱用 """
    # True
    judge_3_1 = type(b) is B
    # True
    judge_3_2 = type(b) == B
    # False
    judge_3_3 = type(b) is A
    print(judge_3_1)
    print(judge_3_2)
    print(judge_3_3)
    print(judge_3)


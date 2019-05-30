# -*- coding: utf-8 -*-
from collections.abc import Sized

"""
    描述：
        抽象基类（abc 模块）, 类似于静态语言(java...)里的接口
    应用场景：
        1. 检查某个类是否有某种方法
        2. 需要强制某个子类必须实现某些方法
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        """
            描述：只需要申明该函数，该类就是集合、序列
        """
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


if __name__ == '__main__':
    com = Company(['Tom1', 'Tom2'])

    # 方法一
    # hasattr 判断 Company 这个对象是否有 __len__
    length = hasattr(com, '__len__')
    print(length)

    # 方法二 使用抽象基类来判断
    length = isinstance(com, Sized)
    print(length)




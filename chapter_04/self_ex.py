# -*- coding: utf-8 -*-

"""
    描述：
            Python 中的自省机制
            自省：自省是通过一定的机制查询到对象的内部结构
"""


class Person:
    """
        人
    """
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("清华大学")

    # 通过 __dict__ 查询属性
    res = user.__dict__
    user.__dict__["school_name"] = "北京大学"
    # mro 向上查找到 Person 找到 name
    info = user.name
    print(info)
    print(res)
    print(Person.__dict__)

    # 列出对象的所有属性
    res_dir = dir(user)
    print(res_dir)

    a = [1, 2]
    print(dir(a))

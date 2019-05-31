# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 23:37
from datetime import datetime, date
"""
    描述：
        __getattr__: 查找不到属性的时候调用
        __getattribute__： 
        __getattribute__ 优先级比 __getattr__ 高
"""


class User(object):
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "Tom"


if __name__ == '__main__':
    user = User('Tom', date(year=1992, month=5, day=31), info={"company_name": "清华大学"})
    # print(user.age)
    # print(user.name)

    print(user.company_name)

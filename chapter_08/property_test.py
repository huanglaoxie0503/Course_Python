# -*- coding: utf-8 -*-
from datetime import date, datetime
"""
    描述：
        property 属性 (动态属性)、属性描述符
"""


class User(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('Tom', date(year=1992, month=5, day=31))
    print("in {0} file".format(__file__))

    res = user.get_age()
    print(res)

    res_01 = user.age
    print(res_01)

    # 属性赋值
    user.age = 20
    print(user.age)
    print(user._age)




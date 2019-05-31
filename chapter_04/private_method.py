# -*- coding: utf-8 -*-
from chapter_04.class_method import NewDate
"""
    描述：
        Python 中的数据封装和私有属性
"""


class User:
    def __init__(self, birthday):
        # 私有属性
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2019 - self.__birthday.year


if __name__ == '__main__':
    user = User(NewDate(1992, 2, 1))

    print(user.get_age())

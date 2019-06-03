# -*- coding: utf-8 -*-
from collections.abc import Iterator

"""
    迭代器和可迭代对象
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


# class MyIterator(object):
#     def __iter__(self):
#         return self


class MyIterator(Iterator):
    """
        自定义迭代器
    """
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    name_list = ["tom", "bob", "jane", "321"]
    company = Company(name_list)

    # my_iter = iter(company)
    # while True:
    #     try:
    #         print(next(my_iter))
    #     except StopIteration:
    #         pass

    for info in company:
        print(info)

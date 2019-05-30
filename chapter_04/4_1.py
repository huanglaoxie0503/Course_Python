# -*- coding: utf-8 -*-

"""
    鸭子类型和多态
"""


class Cat(object):
    def say(self):
        print('I am Cat')


class Dog(object):
    def say(self):
        print('I am Dog')


class Duck(object):
    def say(self):
        print('I am Duck')


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


# animal = Cat
# animal().say()

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Animal(object):
    def say(self):
        pass


if __name__ == '__main__':
    company = Company(['tom', 'bob', 'jane'])

    a = ['Tom1', 'Tom2']
    b = ['Tom2', 'Tom1']
    name_tuple = ('Tom3', 'Tom4')
    name_set = set()
    name_set.add('Tom5')
    name_set.add('Tom6')

    # extend 会调用对象（list, tuple, set）里的方法，如：__getitem__ (可迭代对象)
    # a.extend(name_tuple)
    # print(a)

    # a.extend(name_set)
    # print(a)

    # company 对象里申明了 __getitem__ ，company 对象就可以和 list, tuple, set 一样操作
    a.extend(company)
    print(a)


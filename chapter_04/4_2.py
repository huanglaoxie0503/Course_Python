# -*- coding: utf-8 -*-
import abc

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
            描述：
                只需要申明该函数，该类就是集合、序列
        """
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


class CacheBase(metaclass=abc.ABCMeta):
    """
        描述：
            实现抽象基类(协议或者约定)
    """
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    """
        描述：
            实现 redis 缓存
        备注：
            RedisCache 对象继承自 CacheBase，而 CacheBase 是抽象基类，所以 RedisCache 必须实现 CacheBase 里的所有方法, 否则报错：
            TypeError: Can't instantiate abstract class RedisCache with abstract methods get
    """
    def set(self, key, value):
        pass

    def get(self, key):
        pass


if __name__ == '__main__':
    com = Company(['Tom1', 'Tom2'])

    # 方法一
    # hasattr 判断 Company 这个对象是否有 __len__
    length = hasattr(com, '__len__')
    print(length)

    # 方法二 使用抽象基类来判断
    length = isinstance(com, Sized)
    print(length)

    redis_cache = RedisCache()
    redis_cache.set('key', 'value')




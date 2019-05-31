# -*- coding: utf-8 -*-

"""
    描述：
        Python 中的类方法、静态方法、实例方法（对象方法）及参数
"""


class NewDate:
    # 以下都是实例化方法
    def __init__(self, year, month, day):
        """
            构造函数
        """
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        # 静态方法
        year, month, day = tuple(date_str.split('-'))
        return NewDate(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and int(month) < 12) and int(day) > 0 and int(day) <= 31:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        # 类方法
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = NewDate(2018, 12, 13)
    new_day.tomorrow()
    print(new_day)

    # 2018-12-31
    date = '2018-12-33'
    # 用 普通方法 完成初始化
    # year, month, day = tuple(date.split('-'))
    # print(year, month, day)
    # new_day = NewDate(int(year), int(month), int(day))
    # print(new_day)

    # 用 staticmethod 完成初始化
    new_day = NewDate.parse_from_string(date)
    print(new_day)

    # 用 classmethod 完成初始化
    new_day = NewDate.from_string(date)
    print(new_day)

    print(NewDate.valid_str(date))







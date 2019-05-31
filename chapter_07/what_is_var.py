# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 23:03

"""
    描述：
        Python 中的变量实质上是一个指针
"""

a = 1
b = "abc"

# 1. a 贴在 1 上面
# 2. 先生成对象，然后贴便利贴

aa = [1, 2, 3]
bb = aa
print(aa is bb)
print(id(aa), id(bb))
bb.append(4)
print(aa)


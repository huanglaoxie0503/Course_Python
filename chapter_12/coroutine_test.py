# -*- coding: utf-8 -*-
import time

"""
    传统函数调用过程：A-->B-->C
    我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数继续执行,这个函数就叫“协程”
    协程：有多个入口的函数，可以暂停的函数（可以向暂停的地方传入值）
"""

"""
1.生成器不只可以产出值，还可以接收值(调用方传递进来的值)。
2.启动生成器的方式有2种，next(),send()
3. 
"""


def gen_func():
    # 生成器不只可以产出值，还可以接收值(调用方传递进来的值)。
    html = yield "http://kuaixun.stcn.com/index.shtml"
    print(html)
    yield 2
    yield 3
    return 'Tom'


if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器的方式有2种，next(),send(),在调用send()发送非None值之前，我们必须启动一次生成器，方式有2种：gen.send(None)、next(gen)
    url = next(gen)
    # url = gen.send(None)
    html = 'Tom'
    # send 方法可以传递值进入生产器内部，同时还可以重启生成器执行到下一个 yield 位置
    print(gen.send(html))




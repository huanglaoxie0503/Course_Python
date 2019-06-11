# -*- coding: utf-8 -*-


def gen_func():
    # 生成器不只可以产出值，还可以接收值(调用方传递进来的值)。
    yield "http://kuaixun.stcn.com/index.shtml"
    yield 2
    yield 3
    return 'Tom'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    print('Bob')

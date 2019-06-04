# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor

"""
    Python 中的线程池:
        主线程中可以获取某一线程或者某一状态以及返回值
        当一个线程完成的时候我们主线程能立即知道
        futures 可以让多线程和多进程编码接口一致
"""


def get_html(times):
    time.sleep(times)
    print("get page {0} success".format(times))
    return times


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    # 通过 submit 函数提交执行函数到线程池中, submit 是立即返回，不是阻塞
    task_1 = executor.submit(get_html, (3))
    task_2 = executor.submit(get_html, (2))

    # done() 方法用于判定某个人物是否完成
    print(task_1.done())
    time.sleep(3)
    print(task_1.done())




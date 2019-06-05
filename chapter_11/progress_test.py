# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

"""
    Python 中的多进程编程
        1. 耗 CPU 的操作，用多进程；对于 IO 操作来说，使用多线程
        2. 对操作系统来说，进程切换代价要高于线程切换
        3. 对于耗 CPU 的操作，如：计算、挖矿，多进程优于多线程
"""


# 对于耗 CPU 的操作，如：计算、挖矿，多进程优于多线程
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


# 对于 IO 操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    # 1. 耗 CPU 的操作,多线程和多进程对比
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {0}".format(data))

    print("多线程-last time is :{0}".format(time.time() - start_time))

    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {0}".format(data))

    print("多进程-last time is :{0}".format(time.time() - start_time))

    # 2. IO 操作，多线程和多进程对比
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {0}".format(data))

    print("多线程-last time is :{0}".format(time.time() - start_time))

    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {0}".format(data))

    print("多进程-last time is :{0}".format(time.time() - start_time))




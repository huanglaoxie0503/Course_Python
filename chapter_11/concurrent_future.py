# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED

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

    # 1. 通过 submit 函数提交执行函数到线程池中, submit 是立即返回，不是阻塞
    task_1 = executor.submit(get_html, (3))
    task_2 = executor.submit(get_html, (2))

    # done() 方法用于判定某个人物是否完成
    print(task_1.done())
    # 取消任务
    # print(task_2.cancel())
    time.sleep(5)
    print(task_1.done())

    # result 方法可以获取 task 的执行结果
    print(task_1.result())

    # 2. 要获取已经成功的 task 的返回
    urls = [3, 2, 4]
    all_task = [executor.submit(get_html, (url)) for url in urls]
    # wait 可以让主线程阻塞
    wait(all_task, return_when=FIRST_COMPLETED)
    print('main Thread')
    time.sleep(10)
    for future in as_completed(all_task):
        data = future.result()
        print("get {0} page success".format(data))

    # 3. 通过 executor 获取已经完成的 task
    if __name__ == '__main__':
        for data in executor.map(get_html, urls):
            print("get {0} page ".format(data))





# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

"""
    多进程编程之 multiprocessing，它比 ProcessPoolExecutor 更底层，一般推荐使用 ProcessPoolExecutor 方式实现多进程
"""


def get_html(n):
    time.sleep(n)
    print("sub_process success")
    return n


class MyProcess(multiprocessing.Process):
    def run(self):
        pass


if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2, ))
    print(process.pid)
    process.start()
    print(process.pid)
    process.join()
    print("main process end")

    # 使用线程池(multiprocessing 里的线程池)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3, ))

    # 等待所有任务完成
    pool.close()
    pool.join()
    print(result.get())

    # imap 方法 按列表顺序输出
    for result in pool.imap(get_html, [1, 5, 3, 2, 6]):
        print("{} sleep success".format(result))

    # imap_unordered  谁先完成先输出谁
    for result in pool.imap_unordered(get_html, [1, 5, 3, 2, 6]):
        print("{} sleep success".format(result))


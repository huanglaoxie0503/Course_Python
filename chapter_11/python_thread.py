# -*- coding: utf-8 -*-
import time
import threading

"""
        Python 中的多线程
        1. 对于 io 操作来说，多线程和多进程差别不大
"""


def get_detail_html(url):
    print("get_detail_html_started")
    time.sleep(2)
    print("get_detail_html_end")


def get_detail_url(url):
    print("get_detail_url_started")
    time.sleep(4)
    print("get_detail_url_started")


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get_detail_html_started")
        time.sleep(2)
        print("get_detail_html_end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    print("get_detail_url_started")
    time.sleep(2)
    print("get_detail_url_started")


if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=("", ))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    # # 设置为守护线程
    # # thread1.setDaemon(True)
    # # thread2.setDaemon(True)
    # start_time = time.time()
    #
    # thread1.start()
    # thread2.start()
    #
    # # 阻塞线程，等子线程结束在执行主线程
    # thread1.join()
    # thread2.join()
    #
    # # 当主线程退出后，子线程 kill
    #
    # print("last time:{0}".format(time.time()-start_time))

    start_time = time.time()
    thread_class_1 = GetDetailHtml("get_detail_html")
    thread_class_2 = GetDetailUrl("get_detail_url")

    thread_class_1.start()
    thread_class_2.start()

    thread_class_1.join()
    thread_class_2.join()

    print("last time:{0}".format(time.time() - start_time))




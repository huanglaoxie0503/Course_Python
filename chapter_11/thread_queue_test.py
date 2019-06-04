# -*- coding: utf-8 -*-
import threading
import time

from queue import Queue


"""
    通过 Queue 的方式进行线程间通信
"""


def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get_detail_html_started:{0}".format(url))
        time.sleep(2)
        print("get_detail_html_end:{0}".format(url))


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        time.sleep(2)
        for k in range(10):
            print("get_detail_url_started")
            queue.put("http://blog.jobbole.com/{0}".format(k))
            print("get_detail_url_end")


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        thread_detail_html.start()

    start_time = time.time()

    detail_url_queue.task_done()
    detail_url_queue.join()

    print("last time:{0}".format(time.time() - start_time))

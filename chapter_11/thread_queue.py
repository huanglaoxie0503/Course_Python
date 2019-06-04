# -*- coding: utf-8 -*-
import time
import threading

from chapter_11 import variables

"""
    线程间通信:
        1.共享变量(不推荐)
        2. Queue
"""


def get_detail_html():
    # 爬取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get_detail_html_started:{0}".format(url))
            time.sleep(2)
            print("get_detail_html_end:{0}".format(url))


def get_detail_url(url):
    # 爬取文章列表页
    while True:
        time.sleep(4)
        for k in range(50):
            print("get_detail_url_started")
            variables.detail_url_list.append("http://blog.jobbole.com/{0}".format(k))
            print("get_detail_url_end")


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(variables.detail_url_list, ))
    thread_detail_url.start()
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(variables.detail_url_list, ))
        thread_detail_html.start()


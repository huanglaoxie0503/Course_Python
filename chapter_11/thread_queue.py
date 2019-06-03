# -*- coding: utf-8 -*-
import time
import threading

"""
    线程间通信:
        1.共享变量
"""

detail_url_list = []


def get_detail_html(url):
    # 爬取文章详情页
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
        for i in range(50):
            print("get_detail_url_started")
            detail_url_list.append("http://blog.jobbole.com/{0}".format(i))
            print("get_detail_url_end")


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list, ))
    thread_detail_url.start()
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_list, ))
        thread_detail_html.start()


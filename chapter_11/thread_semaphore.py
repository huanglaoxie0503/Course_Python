# -*- coding: utf-8 -*-
import threading
import time

"""
    Semaphore 是用于控制进入数量的锁
    
    文件的读、写：
        写一般只适用于一个线程, 读可以允许有多个。
"""


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("get html text success\n")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{0}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    semaphore = threading.Semaphore(4)
    url_producer = UrlProducer(semaphore)
    url_producer.start()


# -*- coding: utf-8 -*-
import time
from multiprocessing import Process, Queue
# from queue import Queue


"""
    进程间通信: multiprocessing 里的 Queue 来实现
"""


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    queue = Queue(10)

    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()


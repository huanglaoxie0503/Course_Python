# -*- coding: utf-8 -*-
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe


"""
    进程间通信: 
              multiprocessing 里的 Queue 来实现
              multiprocessing 里的 Queue 不能用于 pool 进程池, pool 进程池中的进程间通信需要使用 Manager 中的 Queue 来实现
    
    共享全局变量不能用于多进程
    
    三个Queue：
    1. from queue import Queue
    
    2. from multiprocessing import Queue
    
    3. from multiprocessing import Manager
       Manager().Queue()
"""


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


def producer_pipe(pipe):
    pipe.send("Tom")


def consumer_pipe(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    # 1. 进程间通信
    queue_base = Queue(10)

    my_producer = Process(target=producer, args=(queue_base,))
    my_consumer = Process(target=consumer, args=(queue_base,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()

    # 2. 进程池实现进程间通信
    queue_pool = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue_pool,))
    pool.apply_async(consumer, args=(queue_pool,))

    pool.close()
    pool.join()

    # 3. 通过 Pipe（管道） 实现进程间通信
    receive_pipe, send_pipe = Pipe()
    # pipe 只适用于两个进程
    my_producer_pipe = Process(target=producer_pipe, args=(send_pipe,))
    my_consumer_pipe = Process(target=consumer_pipe, args=(receive_pipe,))

    my_producer_pipe.start()
    my_consumer_pipe.start()
    my_producer_pipe.join()
    my_consumer_pipe.join()

    # 4. 共享数据结构：Manager().dict() 实现进程间通信
    progress_dict = Manager().dict()

    first_progress = Process(target=add_data, args=(progress_dict, "Tom1", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "Tom2", 23))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)



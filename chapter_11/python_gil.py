# -*- coding: utf-8 -*-
import threading
from threading import Lock, RLock

"""
    GIL 使得同一个时刻只有一个线程在一个 CPU 上执行字节码，无法将多个线程映射到多个 CPU 上
    GIL 会根据执行的字节码行数以及时间片释放gil，GIL在遇到 IO 操作的时候会主动释放gil
    缺点：
        1. 使用锁会影响性能
        2. 使用锁会引起死锁（锁没有释放）
        
    RLock: 在同一个线程里，可以连续多次调用 acquire,  但是一定要注意 acquire 的次数一定要和 release 一样。
"""


total = 0
lock = Lock()

r_lock = RLock()


def add():
    global total
    # global lock
    global r_lock
    for i in range(1000000):
        lock.acquire()
        do_something(lock)
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


def do_something(lock):
    lock.acquire()
    # do something
    lock.release()


def add_1(a):
    a += 1


def desc_1(a):
    a -= 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)

    """
        字节码解释 add_1 执行过程：
            1. load a
            2. load 1
            3. 执行 + 
            4. 赋值给 a
            
        字节码解释 desc_1 执行过程：
             1. load a
            2. load 1
            3. 执行 -
            4. 赋值给 a
    """

    # import dis
    #
    # print(dis.dis(add_1))
    # print(dis.dis(desc_1))

# -*- coding: utf-8 -*-
import threading

"""
    GIL 使得同一个时刻只有一个线程在一个 CPU 上执行字节码，无法将多个线程映射到多个 CPU 上
    GIL 会根据执行的字节码行数以及时间片释放gil，GIL在遇到 IO 操作的时候会主动释放gil
"""


total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)

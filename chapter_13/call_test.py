# -*- coding: utf-8 -*-
import asyncio

"""
asyncio 里的函数:
    call_soon()
    call_soon_threadsafe()
    call_later()
    call_at()
"""


def callback(sleep_times):
    print("sleep {0} success".format(sleep_times))


def stop_loop(loop_):
    # 暂停 loop
    loop_.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()

    # loop.call_soon(callback, 2)
    # loop.call_soon(stop_loop, loop)

    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)

    loop.call_at(now+2, callback, 2)
    loop.call_at(now+1, callback, 1)
    loop.call_at(now+3, callback, 3)

    loop.call_soon(callback, 4)

    loop.run_forever()


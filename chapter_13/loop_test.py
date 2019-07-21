# -*- coding: utf-8 -*-
import asyncio
import time
from functools import partial

"""
事件循环
事件循环+回调（驱动生成器）+ epoll(IO多路复用)
asyncio 是 Python 用于解决异步IO编程的一套解决方案, 例如：tornado gevent twisted（scrapy django channels）
tornado(实现web服务器,可以直接部署)，django+flask(uwsgi,gunicorn+nginx)

1.使用 asynico
2.获取协程的返回值
3.wait 和 gather 的区别：
    gather 更加高层，
"""

# 使用 asynico


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


# 获取协程的返回值
async def get_html_value(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "Tom"


def callback(url, future):
    print(url)
    print("send email summer")


# wait 和 gather
async def get_html_wait_gather(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()

    tasks = [get_html("http://kuaixun.stcn.com/index_{0}.shtml".format(i)) for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time()-start_time)

    # 以下2种方式用法一样
    # 源码里还是调用loop.create_task() 实现
    # get_future = asyncio.ensure_future(get_html_value("http://kuaixun.stcn.com/index.shtml"))
    # 协程注册到 loop 里
    task = loop.create_task(get_html_value("http://kuaixun.stcn.com/index.shtml"))
    # 添加一个函数 ，partial把一个函数包装成一个参数
    task.add_done_callback(partial(callback, "http://kuaixun.stcn.com/index.shtml"))

    loop.run_until_complete(task)
    print(task.result())

    tasks = [get_html_wait_gather("http://kuaixun.stcn.com/index.shtml") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time()-start_time)

    # wait 和 gather 的区别：
    # gather 更加高层
    group1 = [get_html_wait_gather("http://kuaixun.stcn.com/index.shtml") for i in range(2)]
    group2 = [get_html_wait_gather("https://www.cls.cn/") for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)

    loop.run_until_complete(asyncio.gather(group1, group2))




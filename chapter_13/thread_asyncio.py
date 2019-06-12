# -*- coding: utf-8 -*-
import asyncio
import time
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

"""
asyncio: 异步IO解决方案
多线程+协程(不能加阻塞IO)
使用多线程，在协程中集成阻塞IO
"""


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立 socket 链接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 阻塞不会消耗CPU
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)
    tasks = []
    for _url in range(1, 53):
        _url = "http://shop.projectsedu.com/goods/{}/".format(_url)
        task = loop.run_in_executor(executor, get_url, _url)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:{}".format(time.time() - start_time))



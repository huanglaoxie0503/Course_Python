# -*- coding: utf-8 -*-
import asyncio
import time
from urllib.parse import urlparse


"""
asyncio 模拟 http请求
asyncio 没有提供 http 协议接口
"""


async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立 socket 链接
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf-8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html


async def run_main(loop):
    tasks = []
    for url in range(1, 20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(asyncio.ensure_future(get_url(url)))

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    # tasks = []
    # for _url in range(1, 20):
    #     _url = "http://shop.projectsedu.com/goods/{}/".format(_url)
    #     tasks.append(asyncio.ensure_future(get_url(_url)))

    loop.run_until_complete(run_main(loop))

    print("last time:{}".format(time.time() - start_time))



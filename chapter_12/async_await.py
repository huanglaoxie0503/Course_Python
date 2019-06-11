# -*- coding: utf-8 -*-

"""
Python 为了将语义变得更加明确，引入了async和await关键字用于定义原生协程
"""


async def downloader(url):
    # async 里不能用 yield
    return "小米"


async def download_url(url):
    # do something
    html = await downloader(url)
    return html


if __name__ == '__main__':
    result = download_url("http://kuaixun.stcn.com/index.shtml")
    result.send(None)

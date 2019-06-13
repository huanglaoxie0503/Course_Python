# -*- coding: utf-8 -*-
import asyncio
import aiohttp
from asyncio import Lock, Queue


"""
asynico 的同步和通信
"""

total = 0


async def add():
    global total
    for i in range(1000000):
        total += 1


async def desc():
    global total
    for i in range(1000000):
        total -= 1


cache = {}
lock = Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    # do something parsing
    stuff = await get_stuff()


async def use_stuff():
    # use stuff to do something interesting
    stuff = await get_stuff()


if __name__ == '__main__':
    tasks = [add(), desc()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)

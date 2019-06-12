# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 9:17
"""
    IO 多路复用：select、epoll、
    epoll 并不代表一定比 select 好，在并发高的情况下，连接活跃度不是很高，epoll 比 select 好；并发性不高，同时连接很活跃，select 比 epoll 好。

"""
# 通过非阻塞IO实现http
# 回调+事件循环

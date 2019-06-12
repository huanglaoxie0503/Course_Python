# -*- coding: utf-8 -*-
import asyncio
import time


"""
协程嵌套
"""

# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# 1. loop 会被放到future中
# 2. 取消future(task)


async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))


async def computer(x, y):
    print("Computer %s + %s..." % (x, y))
    await asyncio.sleep(2)
    return x + y


async def print_sum(x, y):
    result = await computer(x, y)
    print("%s + %s = %s" % (x, y, result))


if __name__ == '__main__':
    # task1 = get_html(2)
    # task2 = get_html(3)
    # task3 = get_html(3)
    #
    # tasks = [task1, task2, task3]
    #
    # loop = asyncio.get_event_loop()
    #
    # try:
    #     loop.run_until_complete(asyncio.wait(tasks))
    # except KeyboardInterrupt as e:
    #     all_tasks = asyncio.Task.all_tasks()
    #     for task in all_tasks:
    #         print("cancel task")
    #         print(task.cancel())
    #     loop.stop()
    #     loop.run_forever()
    # finally:
    #     loop.close()

    # 协程嵌套
    loop = asyncio.get_event_loop()
    # run_until_complete() 将 print_sum 这个协程注册到loop里
    loop.run_until_complete(print_sum(2, 3))
    loop.close()




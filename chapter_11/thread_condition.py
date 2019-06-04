# -*- coding: utf-8 -*-
from threading import Condition
import threading

"""
    条件变量-Condition： 用于复杂的线程间同步
    
    在调用with condition(Condition的实例) 之后才能调用wait 或者 notify 方法
    
    condition 有2层锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，等待notify方法的唤醒
"""


# class XiaoAi(threading.Thread):
#     def __init__(self):
#         super().__init__(name="小爱")
#
#     def run(self):
#         print("{}: 在".format(self.name))
#
#
# class TianMao(threading.Thread):
#     def __init__(self):
#         super().__init__(name="天猫精灵")
#
#     def run(self):
#         print("{}: 小爱同学".format(self.name))

# 通过 condition 完成协同读诗

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 好啊!".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 君住长江尾".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 共饮长江水".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 此恨何时已".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 定不负相思意".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}: 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 我们来对古诗吧！".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 我住长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 日日思君不见君".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 此水几时休".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 只愿君心似我心".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    condition = Condition()

    xiao_ai = XiaoAi(condition)

    tian_mao = TianMao(condition)

    # 启动顺序很重要

    xiao_ai.start()
    tian_mao.start()


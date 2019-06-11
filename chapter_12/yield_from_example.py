# -*- coding: utf-8 -*-


final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量:", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key+" 销量统计完成！")


def main_num():
    data_sets = {
        "香飘飘牌面膜": [1200, 1500, 3000],
        "小米牌手机": [1200, 1500, 3000],
        "华为笔记本电脑": [1200, 1500, 3000],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        # 预激 middle 协程
        m.send(None)
        for value in data_set:
            # 给协程传递每一组的值
            m.send(value)
        m.send(None)

    print("final_result:", final_result)


if __name__ == '__main__':
    # main_num()

    my_gen = sales_sum("小米手机")
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1500)
    my_gen.send(3000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)

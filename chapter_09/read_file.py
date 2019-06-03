# -*- coding: utf-8 -*-

"""
    运用生成器读取500G 的大文件，该文件比较特殊，只有一行
"""


def my_read_lines(file, new_line):
    buf = ""
    while True:
        while new_line in buf:
            pos = buf.index(new_line)
            yield buf[:pos]
            buf = buf[pos + len(new_line):]
        chunk = file.read(4096*10)
        if not chunk:
            # 说明已经读取到文件末尾
            yield buf
            break
        buf += chunk


if __name__ == '__main__':
    with open('input.txt') as f:
        # 传入句柄和分隔符
        for line in my_read_lines(f, "{|}"):
            print(line)

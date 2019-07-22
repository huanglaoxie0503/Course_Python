# -*- coding: utf-8 -*-
import requests
from lxml import html

L = []


def get_result(pageNo):
    try:
        url = "http://glidedsky.com/level/web/crawler-basic-2?page={0}".format(pageNo)
        headers = {
            "Cookie": "_ga=GA1.2.501680258.1563509581; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1563509581,1563763110; _gid=GA1.2.904152389.1563763111; XSRF-TOKEN=eyJpdiI6IjFjeFVtcmNyRjRLOHZCUVFscXdYVEE9PSIsInZhbHVlIjoiRlpvN0plWWdlWVp2eFZrRnluYVJcLzMycFJQdFhcLzlselFwdTc2ZWFYWTJMUFFBME5BQndaS0JMZU1Gb0I1cUdqIiwibWFjIjoiYmQ4NTJhNTUzYzI1YWQwZjhhZTAyN2IxNWFiZjgyN2I2YTk5OWRiNTQ3NWQ4OTliYTYxZTgzZmJjZTgxY2FkMiJ9; glidedsky_session=eyJpdiI6IjJqRTA4aUZXZTV5Z2tPbkk4aDhETnc9PSIsInZhbHVlIjoiQmNmd2NMb3dhN0JwQUJOZ0duUlwvenpaZzNiVlBhSEJjVFJNV2szXC9qSGIyZEE2eDhabEZ4NXRlRDN4ZW9wQ21xIiwibWFjIjoiY2ExOTU3NjRhZTExZDU4ZGU4YzQ2YWFkMGRiNjhhYzVmNjg1ODdmMjY3NTQ0NGRkNjdiM2UxOTZmOGQ2NDMwNyJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1563763142",
            "Host": "glidedsky.com",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://glidedsky.com/login",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        response = requests.get(url, headers=headers).text
        tree = html.fromstring(response)
        results = tree.xpath('//div[@class="col-md-1"]/text()')
        for row in results:
            row = row.strip()
            L.append(int(row))
            print(row)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for page in range(1, 1001):
        print("抓取：{0}页".format(page))
        get_result(page)
    print(L)
    num = sum(L)
    print('最后结果：{0}'.format(num))


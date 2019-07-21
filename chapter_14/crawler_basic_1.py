# -*- coding: utf-8 -*-
import requests
from lxml import html


def get_result():
    try:
        url = "http://glidedsky.com/level/web/crawler-basic-1"
        headers = {
            "Cookie": "_ga=GA1.2.105422049.1563704025; _gid=GA1.2.1961136862.1563704025; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1563704024,1563704120; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1563714412; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6InJvekVQU0tid2lHN1JudGE1azNGXC9BPT0iLCJ2YWx1ZSI6IkVVVUN5TENqbURaK2YxbXJkRnp0RU1sVUdCMktVRVwvYWFRNmRGVEJvamVWaEtSaE5TSUdLNGtqb1hsVnhzQyt6IiwibWFjIjoiNGNmMDRiZDBlZWViNjA0MzZhYjMwMjM3ODQyN2U3NzUwNzgyMDA2MWNjNjcwZDU1MTk4NjY4YmVhMTI0NThhMyJ9; glidedsky_session=eyJpdiI6Ilk3ZGVVTXRBUTQ3THhcL2lVcE5pUkFBPT0iLCJ2YWx1ZSI6Im1CODdSU0VhbXBTYWR2Yk1lb1FKWVg1c0hmNlJtSnN2MjJObW10YjBcL2t3VmhTT0xGZWJWeXFWVUZPVXlNZVh1IiwibWFjIjoiNDE5NGQxNTI3YjFiNTE0YTRiZjRhMmVhZmFmYTdjNjU5NTc1ZDc3ZDBmNDFkNzY1NThmM2NlZjY0N2I5YmRhMCJ9",
            "Host": "glidedsky.com",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://glidedsky.com/login",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        response = requests.get(url, headers=headers).text
        tree = html.fromstring(response)
        results = tree.xpath('//div[@class="col-md-1"]/text()')
        rows = []
        for row in results:
            row = row.strip()
            rows.append(int(row))
            print(row)

        num = sum(rows)
        print(num)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_result()


# -*- coding: utf-8 -*-
import requests


def get_html():
    try:
        url = "https://www.xiniudata.com/api/search2/company/lib"
        headers = {
            "cookie": "btoken=REH46A0EY4DFX1M08ACUSGVMNQ6O74DB; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1563786975; _ga=GA1.2.379858316.1563786977; _gid=GA1.2.1059013869.1563786977; _gat_gtag_UA_119390984_1=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1563787003",
            "origin": "https://www.xiniudata.com",
            "referer": "https://www.xiniudata.com/project/lib",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        data = {
            "payload": "LBcgWUQrZGATHHVgSiogJ1Z2DG9kfnZeIi0zOT8qXG1tbhkUEjonPWp7Ah8UZywsXjhZQxtoD29hbCsoOildOAhBJV8SdB0HZGM9LVUgJj1bNxQOGyYmRyhsfm8wMFwrPlsjZ1QvMj9qewIfFGc8J0IhQhYDcHYebyEgKTM3EHV1USFLU2xqeDsuKzYaf2J/AmQCGBsiNVUobGh9emdBJi1QZgICfjs=",
            "sig": "DD2BC59355FD050B5850814DC002C693",
            "v": 1
        }
        resp = requests.post(url, headers=headers, data=data).text
        print(resp)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_html() 


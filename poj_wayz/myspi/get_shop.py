

# coding:utf-8
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""
from __future__ import print_function
import requests
# 请求示例 url 默认请求参数已经做URL编码
url = "http://api01.idataapi.cn:8000/hotel/idataapi?kw=维也纳&apikey=KoUTR752HOS1QF53A5LUKPBYFRUVBohkwMd96Y8nEd2OrQ96MxNVXfpjKa7Gzrcn"
headers = {
"Accept-Encoding": "gzip",
"Connection": "close"
}
if __name__ == "__main__":
    r = requests.get(url, headers=headers)
    json_obj = r.json()
    print(json_obj)
    print(json_obj['hasNext'])
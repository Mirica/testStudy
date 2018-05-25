#! /usr/bin/env python
# coding = utf-8

import requests
url = 'http://japi.juhe.cn/qqevaluate/qq'
par = {
    'key ':'dddd',
    'qq ':'123453565'
    }
r = requests.get(url,params = par)
print(r.text)
print(r.status_code)
print(r.headers)
result = r.json()

reason = result['reason']
print(reason)

getUrl = ''

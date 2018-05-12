#! /usr/bin/env python
# coding = utf-8

import requests #http协议
url = 'http://japi.juhe.cn/qqevaluate/qq'
par = {
    'key ':'dddd',
    'qq ':'123453565'
    }
r = requests.get(url,params = par)
print(r.text)
result = r.json()

reason = result['reason']
print(reason)
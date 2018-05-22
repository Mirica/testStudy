#! /usr/bin/env python
# coding = utf-8
import requests
url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
r = requests.session()
y = r.get(url)
print(y.json())
u = y.json()
print(type(y.json()))
print(u['data'][1]['context'])
i= u['data'][1]['context']
if '已经签收'in i:
    print('已经签收啦，去取快速吧')
elif '派送' in i:
    print('快递哥哥在派送啦')
else:
    print('接着等待吧')

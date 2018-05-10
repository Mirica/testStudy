#! /usr/bin/env python
# coding : utf-8
'''
import requests
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
'''
#打印一颗圣诞树
height = 5
starts = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * starts))
    starts += 2
print((' '*height) + '|')

def b():
    b =1
    def bchange():
        nonlocal b
        b += 1
    bchange()
    print(b)

li = [1,2,3,4,5] #从左往右取
l1 = li[-3::1]#最后一个为负数，则从后往前
print(l1)
del li[0]
li.append(8)
print(li)
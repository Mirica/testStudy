#! /usr/bin/env python
# coding = utf-8
import requests
# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#  InsecureRequestWarning) 去掉警告
import urllib3
urllib3.disable_warnings()

#简单的get请求（无参数）
url1 = 'https://www.juhe.cn/loginStatus'
r5 = requests.get(url1,verify = False)
print(r5.text)
print(r5.status_code) #状态码
print(r5.headers)#头部
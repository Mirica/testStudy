#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
#login = requests.session()
login_url = 'http://192.168.1.141:11012/login/success1'
login_par = {'account':'18301256396',
             'pwd':'123456'}
login_hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
login= requests.post(url=login_url,params = login_par,headers =login_hea)
print(login.cookies)
cookies_dic = login.cookies.get_dict()
cookie = []
for i in cookies_dic.keys():
    cookie.append(i + '=')
    cookie.append(cookies_dic[i])
    cookie.append(';')
cookie_str = ''.join(cookie)
print(cookie_str)
print(type(cookie_str))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
login = requests.session()
login_url = 'http://192.168.1.141:11012/login/success1'
login_par = {'account':'18301256396',
             'pwd':'123456'}
login.post(url=login_url,params = login_par)
print(login.cookies)
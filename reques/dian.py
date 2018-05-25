#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
h = webdriver.Firefox()
h.get('http://192.168.1.141:11012/login/index')
time.sleep(1)
h.find_element_by_id('user-name').send_keys('18301256396')
h.find_element_by_id('user-pwd').send_keys('123456')
h.find_element_by_id('login').click()
time.sleep(5)
h.find_element_by_class_name('guanbi').click()
#h.find_element_by_class_name('current').click()
h.find_element_by_id('quit').click()

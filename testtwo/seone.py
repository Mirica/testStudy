#! /usr/bin/env python
# coding = utf-8

from selenium import  webdriver
driver = webdriver.Chrome()
driver.get('https://ww.baidu.com')
print(driver.title)


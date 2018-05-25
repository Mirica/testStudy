#! /usr/bin/env python
# coding = utf-8
import selenium
from selenium import  webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox()
#browser =webdriver.Firefox(firefox_binary=binary)
browser.get('http://www.baidu.com')
browser.set_window_size(1920,1080)
browser.find_element_by_id('kw').send_keys('123')
browser.find_elements_by_name('tj_trnews').click()
#browser.quit()


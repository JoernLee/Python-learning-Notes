# -*- coding:utf-8 -*-
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
# 搜索

browser.find_element_by_id("kw").send_keys('selenium')
time.sleep(3)

browser.maximize_window()
js = "var q=document.body.scrollTop=5000"
# 此方法适用于chrome浏览器 针对IE和firebox 使用document.documentElement.scrollTop = 300
browser.execute_script(js)
time.sleep(3)

browser.quit()

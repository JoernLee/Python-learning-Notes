# -*- coding:utf-8 -*-
from selenium import webdriver
import time

browser = webdriver.Chrome()    # select browser
browser.get('http://www.baidu.com')
print '浏览器最大化'

browser.maximize_window()
browser.implicitly_wait(20) # 等待上一个命令完成
# 下面是测试前进和后退的
"""
first_url = 'http://www.baidu.com'
print 'now access %s' % first_url
browser.get(first_url)
time.sleep(3)

second_url = 'http://news.baidu.com'
print 'now access %s' % second_url
browser.get(second_url)
time.sleep(3)

print 'back to %s' % first_url
browser.back()
time.sleep(1)

print 'forward to %s' % second_url
browser.forward()
time.sleep(2)
"""
# id = cp 的元素的文本信息
data = browser.find_element_by_id('cp').text
print data
time.sleep(3)
# 搜索信息
browser.find_element_by_id('kw').send_keys('selenium')  # 一个控件有若干个属性，而百度输入框的id叫kw
browser.find_element_by_id('su').submit()
# browser.find_element_by_id('su').click()                # 搜索按键的id
# browser.find_element_by_partial_link_text('贴吧').click()
time.sleep(3)
browser.quit()     # close the windows and clear connected drivers
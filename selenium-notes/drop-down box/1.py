# -*- coding:utf-8 -*-
from selenium import webdriver
import os, time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

browser.find_element_by_link_text('设置').click()
browser.find_element_by_link_text('搜索设置').click()
time.sleep(2)
m = browser.find_element_by_id('se-setting-3')
browser.find_element_by_xpath("//option[@value='20']").click()
time.sleep(1)

# 保存设置的信息
browser.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)
alert = browser.switch_to.alert
print alert.text
alert.accept()
time.sleep(1)
# 跳转到百度首页后，进行搜索表（一页应该显示20条结果）
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
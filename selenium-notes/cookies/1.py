# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')
time.sleep(1)

driver.add_cookie({'name':'key-aaaaaa', 'value': 'value-bbbbbb'})

for cookie in driver.get_cookies():
    print '%s -> %s' % (cookie['name'], cookie['value'])
# driver.delete_cookie('CookieName')
# driver.delete_all_cookies()

time.sleep(1)
driver.quit()
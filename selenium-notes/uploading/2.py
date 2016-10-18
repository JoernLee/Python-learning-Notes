# -*- coding:utf-8-*-
from selenium import webdriver
import os, time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
browser = webdriver.Chrome()
#打开html文件
file_path = 'file:///' + os.path.abspath('c.html')
browser.get(file_path)
#定位按钮，点击添加本地文件
browser.find_element_by_name('file').send_keys('D:\\1.txt')
time.sleep(2)

browser.quit()

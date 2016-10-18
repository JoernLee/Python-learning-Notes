# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
import time
browser = webdriver.Chrome()  # open the chrome
browser.get("http://www.yahoo.com")
print browser.title
assert 'Yahoo' in browser.title   # make sure the “yahoo” is existing
elem = browser.find_element_by_name('p')  # find the query box to make search
elem.send_keys('selenium'+Keys.RETURN)    # find selenium and press enter
time.sleep(0.2)


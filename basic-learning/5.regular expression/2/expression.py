# -*- coding: UTF-8 -*-
import re
text = "Hi,I am Shirely Hilton. I am his wife"
m = re.findall(r"I.*?e", text)
if m:
    print m
else:
    print "not match"

text2 = "site sea sue sweet see case sse ssee loses"
m2 = re.findall(r"\bs\S*?e\b", text2)  #找出s开头e结尾的单次
if m2:
    print m2
else:
    print "not match"

text3 = "李嘉昕 15161187386"
m3 = re.findall(r"1[0-9]{10}", text3)  #以1开头 后面跟着10位数字
if m3:
    print m3
else:
    print "not match"

text4 = "(021)88776543 010-55667890 02584453362 0571_66345673"
m4 = re.findall(r"1[0-9]{10}", text4)  #以1开头 后面跟着10位数字
if m4:
    print m4
else:
    print "not match"
import urllib2
web = urllib2.urlopen("http://www.baidu.com")
content = web.read()
f = open(r"E:\Python27\learn python\2.check weather\baidu.html", "w")
f.write(content)
f.close()

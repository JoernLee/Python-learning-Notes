# -*- coding: utf-8 -*-
import urllib2
#抓取每个省
url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
print content1
print provinces
result = 'city = {\n'
#抓取每个省对应的市
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib2.urlopen(url2).read()
    print content2
    cities = content2.split(',')
#抓取每个市的区
    for c in cities:
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib2.urlopen(url3).read()
        print content3
        districts = content3.split(',')
#确定最终代码
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib2.urlopen(url4).read()
            print content4
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print  name + ':' + code
result += "}"
f = open(r'E:\Python27\learn python\2.check weathe\record.txt')
f.write(result)
f.close()



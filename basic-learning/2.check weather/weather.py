# -*- coding: utf-8 -*-
import urllib2
import json
from city import city
cityname = raw_input("请输入想要查找的城市天气:\n")
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        print content
        print type(content)
        print type(data)
        result = data['weatherinfo']
        str_temp = ('%s\n%s~%s') % (
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到这个城市'
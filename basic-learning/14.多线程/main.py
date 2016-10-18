# -*- coding:UTF-8 -*-
#下面是使用单一线程来进行豆瓣电影的抓取
import urllib, time, thread

#time_start = time.time()
#data = []
#for i in range(30):
#    print 'request movie',i
#    id = 1764796 + i
#    url = 'https://api.douban.com/v2/movie/subject/%d'% id
#    d = urllib.urlopen(url).read()
#    data.append(d)
#    print i,time.time()-time_start

#print 'data:', len(data)
#下面使用多线程技术
#然而想一下，我们抓一部电影信息的过程是独立，并不依赖于其他电影的结果。因此没必要排好队一部一部地按顺序来。那么有没有
#什么办法可以同时抓取好几部电影？
#答案就是：多线程。
def get_content(i):

    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start
    print 'data:', len(data)

time_start = time.time()
data = []
for i in range(30):
    print 'request movie:', i
    thread.start_new_thread(get_content, (i,))
raw_input('press ENTER to exit...\n')

#从输出结果可以看出：
#在程序刚开始运行时，已经发送所有请求
#收到的请求并不是按发送顺序，先收到就先显示
#总共用时两秒多
#data 里同样记录了所有30条结果

#所以，对于这种耗时长，但又独立的任务，使用多线程可以大大提高运行效率。但在代码层面，可能额外需要做一些处理，保证结果正确。如上例中，如果需要电影信息按 id 排列，就要另行排序。

#多线程通常会用在网络收发数据、文件读写、用户交互等待之类的操作上，以避免程序阻塞，提升用户体验或提高执行效率。

#多线程的实现方法不止这一种。另外多线程也会带来一些单线程程序中不会出现的问题。这里只是简单地开个头。
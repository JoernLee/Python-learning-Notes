#-*-coding:UTF-8-*-
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]  #取其中偶数
print list_2

list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i/2 for i in list_1 if i % 2 == 0]  #取其中偶数
print list_2
#作业 一行代码写出1到100被2 3 5整除的数字，并且用；输出
#list_3 = [i for i>=1 and i<=100 if i % 2 ==0 or i % 3 ==0 or i % 5 ==0]
#print list_3
#下面是答案
print ';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])

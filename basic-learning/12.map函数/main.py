#-*-coding:UTF-8-*-
#假设有一个数列，如何把其中每一个元素都翻倍？
lst_1 = [1,2,3,4,5,6]
lst_2 = []
for item in lst_1:
	lst_2.append(item * 2)
print lst_2
#好一点
lst_1 = [1,2,3,4,5,6]
lst_2 = [i * 2 for i in lst_1]
print lst_2
#使用mapmap 是 Python 自带的内置函数，它的作用是把一个函数应用在一个（或多个）序列上，把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回。

#map 的第一个参数是一个函数，之后的参数是序列，可以是 list、tuple。
lst_1 = [1,2,3,4,5,6]
def double_func(x):
   return x * 2
lst_2 = map(double_func, lst_1)
print lst_2

#求两个数列的和
lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = map(lambda x, y: x + y, lst_1, lst_2)
print lst_3
#对于每组数据中的元素个数，如果有某组数据少于其他组，map 会以 None 来补全这组参数。

#此外，当 map 中的函数为 None 时，结果将会直接返回参数
#组成的列表。如果只有一组序列，会返回元素相同的列表，如果
#有多组数列，将会返回每组数列中，对应元素构成的元组所组成的列表。听上去很绕口是不是……代码试试看就明白了：
lst_1 = [1,2,3,4,5,6,99]
lst_2 = [1,3,5,7,9,11]
lst_3 = map(None, lst_1)
print lst_3
lst_4 = map(None, lst_1, lst_2)
print lst_4
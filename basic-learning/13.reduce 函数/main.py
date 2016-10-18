#-*-coding:UTF-8-*-
#map 可以看作是把一个序列根据某种规则，映射到另一个序列。reduce 做的事情就是把一个序列根据某种规则，归纳为一个输出。
sum = 0
for i in xrange(1, 101):
	sum += i
print sum

#如果用 reduce 函数，就可以写成：

lst = xrange(1, 101)
print lst
def add(x, y):
	return x + y
print reduce(add, lst)
#reduce(function, iterable[, initializer])
#第一个参数是作用在序列上的方法，第二个参数是被作用的序列，这与 map 一致。另外有一个可选参数，是初始值。
#function 需要是一个接收2个参数，并有返回值的函数。它会从序列 iterable 里从左到右依次取出元素，进行计算。每次计算的结果，会作为下次计算的第一个参数。
#提供初始值 initializer 时，它会作为第一次计算的第一个参数。否则，就先计算序列中的前两个值。

#如果把刚才的 lst 换成 [1,2,3,4,5]，那 reduce(add, lst) 就相当于 ((((1+2)+3)+4)+5)。

#所以，在对于一个序列进行某种统计操作的时候，比如求和，或者诸如统计序列中元素的出现个数等（可尝试下如何用 reduce 做到），可以选择使用 reduce 来实现。相对可以使代码更简洁。
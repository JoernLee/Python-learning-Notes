#-*-coding:UTF-8-*-
#lambda表达式,简单单行函数
sum = lambda a,b,c : a+b+c
print sum(1,2,3)

#lambda 参数列表: 表达式
def fn(x):
 return lambda y: x + y

a = fn(2)
print a(3)

#然对于初学者来说，了解 lambda 表达式还有一个重要作用就是，看懂别人写的代码
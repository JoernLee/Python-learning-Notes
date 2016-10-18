#-*-coding:UTF-8-*-
#默认值参数
def func(arg1=1, arg2=2, arg3=3):
	print arg1, arg2, arg3
func(7)
#指定特定位置参数
func(arg2=8)
func(arg3=9, arg1=10)
#但要注意，没有指定参数名的参数必须在所有指定参数名的参数前面，且参数不能重复。以下的调用都是错误的：

#func(arg1=13, 14)
#func(15, arg1=16)

#接受任意数量的参数,调用时候参数存储在一个tuple里面
def calcSum(*args):
	sum = 0
	for i in args:
		sum += i
	print sum
calcSum(1,2,3)
calcSum(123,456)
calcSum()

#最灵活的参数传递，以键值对字典的形式传入
def printAll(**kargs):
	for k in kargs:
		print k, ':', kargs[k]

printAll(a=1, b=2, c=3)
printAll(x=4, y=5)

#前面的多种方法还可以在一起使用
def func(x, y=5, *a, **b):
   print x, y, a, b

func(1)
func(1,2)
func(1,2,3)
func(1,2,3,4)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,k=1,t=2,o=3)

#在混合使用时，首先要注意函数的写法，必须遵守：
#带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
#元组参数(*args)须在带有默认值的形参(arg=)之后；
#字典参数(**kargs)须在元组参数(*args)之后。

#可以省略某种类型的参数，但仍需保证此顺序规则。

#调用时也需要遵守：
#指定参数名称的参数要在无指定参数名称的参数之后；
#不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

#而在函数被调用时，参数的传递过程为：
#1.按顺序把无指定参数的实参赋值给形参；
#2.把指定参数名称(arg=v)的实参赋值给对应的形参；
#3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
#4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。

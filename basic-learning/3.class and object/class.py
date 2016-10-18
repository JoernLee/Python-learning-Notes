class MyClass:
    name = "David"
    def sayHi(self):   #类方法第一个参数必须是self，调用的时候不需添加self
        print "Hello %s" % self.name
my = MyClass()
print my.name
my.name = "LJX"
my.sayHi()

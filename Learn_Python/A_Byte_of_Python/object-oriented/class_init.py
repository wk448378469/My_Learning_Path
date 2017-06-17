#coding=utf-8

class Person:
    def __init__(self,name):           #__init__可以对我们的对象做一些我们希望的初始化。我们把__init__方法定义为取一个参数name（以及普通的参数self）。说白了就是创造一个新的域name
        self.name=name
    def sayHi(self):
        print 'Hello,my name is',self.name

p=Person('wangkai')
p.sayHi()
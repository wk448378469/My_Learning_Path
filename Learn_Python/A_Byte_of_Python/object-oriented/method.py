

class Person():
    def sayHi(self):                     #不需要传入参数，但是python还是给我们定义了一个self的参数
        print 'Hello,how are you?'
p=Person()
p.sayHi()                                #方法一

Person().sayHi()                         #方法二

#This is short example can also be written as Person().sayHi()

#coding=utf-8

class Person:                                         #定义一个类
    '''Represents the person .'''
    population=0                                         #定义个人数的变量赋值0，从属于类
    def __init__(self,name):                             #在整个类里定义个函数，并且做了一个初始化定义个需要传入name     从属于函数（对象）的变量
        '''Initializes the person's data.'''
        self.name=name                                    #在整个函数里，我们把传入给name的内容给self.name
        print '(Initializing %s)'%self.name

        #when this person is created ,he/she adds to the population
        Person.population+=1                           #调用类中的population的变量，并且让ta＋1，这个是全局类中的变量，顾出出了这个函数也有效！！

    def __del__(self):                                #在整个类里定义个什么函数呢9 9 __del__?         对象消失的时候被调用，或者对象不再被使用的时候调用！！
        '''I am dying.'''
        print '%s says bye.'%self.name                 #调用init中的变量
        Person.population-=1                              #调用类中的变量，并让他减一

        if Person.population==0:
            print 'I am the last one'
        else:
            print 'There are still %d people left.'%Person.population

    def sayHi(self):                                            #定义个sayhi函数在类里
        '''Greeting by the person
                Really,that's all it does'''
        print 'Hi,my name is %s.'%self.name

    def howmany(self):                                         #定义个howmany的函数在类里
        '''Prints the current population.'''
        if Person.population==1:
            print 'I am the only person on here'
        else:
            print 'We have %d persons here'%Person.population

swaroop=Person('swaroop')
swaroop.sayHi()
swaroop.howmany()

kalam=Person('Abdul Kalam')
kalam.sayHi()
kalam.howmany()

swaroop.sayHi()
swaroop.howmany()

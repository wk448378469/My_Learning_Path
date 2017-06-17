#coding=utf-8

#代码1——函数的定义和调用
def sayHello():
    print'Hello world!' #block belonging to the function
sayHello()
#记住，在python中，定义函数的名称的时候不要有空格。


#代码2——函数的形参
def printMax(a,b):
    if a>b:
        print a,'is max'
    else:
        print b,'is max'
printMax(4,7)
x=11
y=27
printMax(x,y)
#在打印两个东西的时候切记要用逗号隔开。a,b为形参，传入的4  7是实参


#代码3——局部变量
def func(x):
    print 'x is',x
    x=2
    print 'Changed local x to ',x
x=50
func(x)
print 'x is still',x
#这段代码主要强调的是局部变量，及在函数内改变变量，出了函数就失效。如果想在python中的函数中定义全局变量则需要使用global


#代码4——全局变量
def func():
    global x
    print 'x is',x
    x=2
    print 'Changed local x to',x
x=50
func()
print 'Value of x is',x
#global 将形参x变成了全局变量，顾在调用完函数后x的值仍受函数的影响。此外global也可以定义多个全局变量。eg：global x,y,z


#代码5——使用默认参数
def say(hahah1a,times=1):
    print hahah1a*times
say('Hello')
say('xiang',5)
#如果想函数的参数可选，如果不传入参数的话就使用默认值。这里就会用到默认参数。使用方式就是在定义函数的形参后加=、以及默认值即可。此外在定义形参的时候不要使用全数字。
#注意！！！！形参的最后面的那个参数可以有默认参数值，前面的不可以。eg:def say(a,b=5):可以      而def say（a=5,b):不可以


#代码5——关键参数
def imp(a,b=5,c=10):
    print 'a is',a,'and b is',b,'and c is',c
imp(3,7)
imp(25,c=24)
imp(c=50,a=100)
#就是根据形参的命名来锁定而不需要考虑位置，如果没有使用关键参数的话就会一次传入参数给函数


#代码6——return语句
def maximum(x,y):
    if x>y:
        return x
    else:
        return y
print maximum(7,10)
#在没有return语句的函数中，python默认在函数的最后加入return None的语句。None在python中表示没有任何东西的特殊类型。此外，pass在python中表示一个空的语句块。


#代码7——使用DocStrings
def printMax(x,y):
    '''Prints the maximum of two numbers.
        The two values must be integers.
        这里开始是详细的描述函数的作用'''
    x=int(x) #convert to integer,if possible
    y=int(y)
    if x>y:
        print x,'is maximum'
    else:
        print y,'is maximu'
printMax(3,5)
print printMax.__doc__
#DocStrings被称为文档字符串。调用方式是printMax._doc_   作用让别人能够更好的理解你写的函数。起到说明的作用。
#注意！！！函数的第一行逻辑行是这个函数的“文档字符串”。通用规范是首行大写字母开始，第二行空格，第三行是详细内容


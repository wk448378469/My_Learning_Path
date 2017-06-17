
def normalize(name):
    return name[0].upper()+name[1:len(name)].upper().lower()

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print (L2)

from functools import reduce
def prod(L):
    def X(x,y):
        return x*y
    return reduce(X,L)

print('3*5*7*9=',prod([3,5,7,9]))



def is_odd(n):
    return n%2 == 1
print (list (filter(is_odd,[1,2,3,4,5,6,7,8,9])))
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
    return s and s.strip()
print (list(filter(not_empty,['A','B',' ','1'])))
#strip()是剔除空格或者括号中的任何你想剔除的函数。如果括号中什么都没有就是默认剔除‘ ’


#一个素数的代码！
def _odd_iter():         #构造一个从3开始的奇数
    n = 1
    while True:
        n = n+2
        yield n
def _not_divisible(n):         #然后是一个筛选函数
    return lambda x:x % n>0      #不过这行没看懂有点，应该是做素数的计算用的
def primes():                  #然后做一个生成器，不断的返回下一个素数
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter (_not_divisible(n),it)

for n in primes():
    if n<100:
        print(n)
    else:
        break




#一个回数的代码！
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome,range(1,1000))
print (list(output))



#sorted 排序！
print (sorted([35,7,-1,55,100]))

#sorted 也是高级函数，可以接受一个key函数来实现某些定义
print (sorted([5,-10,55,-9900],key=abs))  #按照绝对值大小

#print (sorted('bob','Zoo','about'))        需要在交互下实现  
#对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。



#分别按照名字和数字排序~
L = [('bob',75),('adam',92),('bart',66),('lisa',81)]
def by_name(t):
    return t[0]
def by_mark(t):
    return t[1]
L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_mark)
print (L2)
print (L3)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#函数作为返回值！可以不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
f1 = lazy_sum(1,3,5,7,9)
print (f1())#就是想调用的时候再显示出来

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print (f1())
print (f2())
print (f3())
#打印的结果全是9
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range (1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print (f1())
print (f2())
print (f3())
#再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。




#匿名函数！！！！
print (list (map(lambda x: x*x,[1,2,3,4,5,6,7,8,9])))
#lambda x: x*x就是匿名函数      冒号前的x表示函数参数！没有返回值，表达式本身就是返回值
#等于
def f(x):
    return x*x




#装饰器！:在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def now():
    print ('asdasdasd')
f = now
f()

print (now.__name__)
print (f.__name__)         #函数对象的一个属性，可以拿到函数的名字


def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print ('2016-3-15')
now()
#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
#装饰器这个等回过头来再看下，还是没看懂~




#偏函数
print (int('12345'))
print (int ('12345',base=8))        #字符串转8进制
print (int ('12345',base=16))         #字符串转16

def int2(x,base=2):
    return int(x,base)
print (int2('10000'))
print (int2('100000'))


import functools
int2 = functools.partial(int,base=2)    #不需要上面这样的自己定义，Python中有抽象出来更好的功能
print (int2('100'))
print (int2('10'))




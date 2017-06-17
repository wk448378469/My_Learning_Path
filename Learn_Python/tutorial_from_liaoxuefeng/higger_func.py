
print(abs(-10))

x = abs(-10)
print(x)

f = abs                       #把函数复制给变量！
print(f(-100))

def add(x,y,f):               #一个高阶函数，函数的参数接受一个函数作为参数
    return f(x)+f(y)
x = -5
y = 6
f = abs
print (add(x,y,f))


def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print (list(r))

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#虽然这个例子是很脑残，因为有其它的方法可以实现~但是传入的函数可以更强大

L = list(map(str,[1,2,3,4,5,6,7]))
print (L)

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。

from functools import reduce
def add(x,y):
    return x + y
print (reduce(add,[1,3,5,7,9]))


def fn(x,y):
    return x*10+y
print (reduce(fn,[1,3,5,7,9]))


#str转为int
def fn(x,y):
    return x*10+y

def char2num (s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print (reduce(fn,map(char2num,'12343234')))

#整理一下

def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))
print (str2int('123124234123'))        



#练习


#切片！（从XX中取出某一段xx）
L = ['wangkai','bob','neak','jack','sarah']
print (L[0],L[1],L[2])

r=[]
n=3
for i in range(n):
    r.append(L[i])    #利用一个空的列表，一次在这个空列表的尾部添加L的内容

print (r)


print (L[0:3])
print (L[:3])
print (L[-2:])
print (L[-2:-1])

number = list(range(100))
print (number)
print (number[0:10])
print (number[:10:2])       #从第一项到第十项，步长2！
print (number[::5])

#tupel 和 字符串也是list的一种，只是有些自己的特性~

tuple1 = tuple(range(6))
print (tuple1[0:3])

myname = 'wangkai'
print (myname[0:4])
print (myname[::2])


#迭代：利用for遍历list tuple等

d = {'a':1,'b':2,'c':3}
for key in d:
    print (key)
for value in d:
    print (value)        #这样的方式只能迭代dict的key，如果想迭代value的话看下面的

for value in d.values():
    print (value)      #but!!!!顺序是乱掉的！（只迭代value）

for k,v in d.items():    #迭代key和value 
    print(k,v)

for ch in 'adc':
    print (ch)

#判断对象是否是可迭代的要用到collection 模块中的Iterable(迭代的意思)

from collections import Iterable
print (isinstance('abc',Iterable))       #'abc'可迭代吗？
print (isinstance([1,2,3],Iterable))     #list 是否可迭代
print(isinstance(123,Iterable))       #整数可迭代吗（不可以）


#enumerate()   可以把list变成索引-元素的形式
for i,value in enumerate (['a','b','c']):
    print (i,value)




#列表生成式
x=list(range(1,11))
print (x)

L = []
for x in range (1,11):
    L.append(x*x)
print (L)

print ([x*x for x in range (1,11)])     #和上面的语句一样的效果！
#第一个是生成的元素，后面跟上一个for循环

print ([x*x for x in range(1,11) if x%2==0])    #真TMD自由！

print ([p + q for p in 'abc' for q in 'xyz'])  #两层循环，可以生成全排列


import os
print ([d for d in os.listdir('D:\wk\'s work')])  #目录下的文件名


d = {'x':'A','y':'B','z':'C'}             #同时使用两个甚至多个变量
for k,v in d.items():
    print (k,'=',v)

d = {'x':'A','y':'B','z':'C'}                 
print ([k + '=' +v for k,v in d.items()])       #把dict变成list

L = ['Hello','World','IBM','Apple']       #把大写变成小写
print ([s.lower() for s in L])



L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print (L2)




#生成器！！！generator
L = [x*x for x in range(10)]
print (L)

g = (x*x for x in range(10))
print (g)
#创建的不同在于，generator是用()来定义列表的
#打印结果是<generator object <genexpr> at 0x1022ef630>
#如果想一个一个打印出来的话就是通过next(g)来获得generator中的下一个返回值
#生成器的作用主要是因为列表生成的时候后面的数据太多，所以不全部扩展，一个一个来
#generator 保存的是算法
#generator 是可迭代的，用for来循环
for x in g:
    print (x)


def fib(max):     #用函数的方法来实现的
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b = b, a+b
        n = n +1
    return 'done'      #著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...

fib(6)              #前方高能！


def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b         #要把fib函数变成generator，只需要把print(b)改为yield b就可以了
        a,b = b, a+b
        n = n+1
    return 'done'
f=fib(6)
print (f)
#如果一个函数中含有yield就不再是函数了，而是generator！！！
#含有yield的generator是不按照顺序执行的。需要输入next()来进行调用！

def odd():
    print ('step 1')
    yield 1
    print ('step 2')
    yield (3)
    print ('step 3')
    yield (5)
o = odd()
print (o)
#同意别傻逼的用next调用，而是用for


for n in fib (6):
    print (n)      #但是for不能拿到return的返回值，必须出现stopiteration才可以

#解决办法
g = fib(6)
while True:
    try:
        x = next(g)
        print ('g:',x)
    except StopIteration as e:
        print ('Generator return value:',e.value)
        break

def triangles():
    Lo=[1]
    yield Lo
    while True:
        Lo.append(0)
        Lo.insert(0,0)
        Lo = [Lo[i]+Lo[i+1] for i in range(len(Lo)-1)]
        yield Lo    
n = 0
for t in triangles():
    print (t)
    n = n+1
    if n ==10:
        break



#










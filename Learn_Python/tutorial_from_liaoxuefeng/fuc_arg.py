

def power(x):              #定义个计算平方的函数
    return x*x
 
print (power(5))


def power (x,n):              #定义个计算x的n次方的函数
    s = 1
    while n>0:
        n = n - 1
        s = s * x
    return s

print (power(5,4))


def power(x,n=2):
    s = 1
    while n>0:
        n = n - 1
        s = s * x
    return s

print (power(5))
print (power(5,5))                  #默认参数的使用方法，要注意的是默认函数一定要在必选函数的后面

def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)

enroll('wangkai','f')

def enroll(name,gender,age=6,city='hangzhou'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('wangkai','x')
enroll('wangkai','q',10)
enroll('wangkai','n','beijing')       #使用默认函数的好处在于调用的难度降低
enroll('wk123','fqa',city='zhalantuan') #也可以指指定


def add_end(L=[]):
    L.append('END')
    print (L)
    return L

add_end([1,2,3])
add_end(['x','y','z'])
add_end()
add_end()     #打印了两个‘end’，Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以一定要记住！！！！！默认参数必须指向不变对象！！！

def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    print(L)
    return L
add_end()
add_end()          #加入一个判断，并且定义的时候用None！


#可变参数！


def calc(numbers):    #计算一组数字的平方和（参数的数量不固定！）
    sum = 0
    for n in numbers:
        sum = sum + n*n
    print (sum)
    return sum
calc([1,2,3])         
calc([1,3,5,7])
  #因为参数的数量不固定，所以我们需要用一个list或者一个tuple组合起我们要传入的参数！

def calc(*numbers):       #调用可变的参数！而不是定义个list or tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    print (sum)
    return sum
calc(1,2,3)
calc(0)

nums = [1,2,3]
calc(*nums)         #把已有的list or tuple传入到函数中！切记加*
#*nums表示把nums这个list的所有元素作为可变参数传进去


#关键字参数！
def person(name,age,**kw):      #name，age是必传参数，kw是关键字参数
    print ('name:',name,'age:',age,'other:',kw)   #*关键字   自动把组装成一个字典！

print (person('Bob',30))
print (person('Bob',35,city='hangzhou'))
print (person('wangkai',45,gender='M',job='student'))
extra = {'city':'Beijing','job':'Engineer'}
print (person('jack',25,city=extra['city'],job=extra['job']))
#也可以先定义一个字典，然后把他传入进去

another = {'city':'zhalantun','job':'teacher'}
print (person('wangkai',25,**another))
#简化一下~   **another表示把another这个字典dict所有key和value用关键字传入到函数的**kw中


#命名关键字参数！
def person (name,age,**kw):
    if 'city' in kw:
        pass
    if 'age' in kw:
        pass
    print ('name:',name,'age:',age,'other:',kw)

person('jack',25,city='beijing',addr='tiananmen',zipcode=123456)



def person (name,age,*,city,job):  #*后面的被认为是命名关键字参数
    print (name,age,city,job)
person('jack',25,city='beijing',job='sdutend')#比如传入关键字！

def person (name,age,*,city='beijing',job):
    print (name,age,city,job)
person ('jack',25,job='teacher')  #可以缺省~及在定义的时候给出默认值


#参数组合！（必选参数、默认参数、可选参数、关键字参数、命名关键字参数）
#顺序！（必选参数、默认参数、可变参数/命名关键字参数、关键字参数）
#还有就是可变参数无法和命名关键字参数混合！

def f1(a,b,c=0,*args,**kw):
    print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print ('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)


#递归函数！！（函数自身调用自身！）

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)      #递归函数的使用！在调用函数前加*
print (fact(5))
print (fact(1))
print (fact(100))       #如果传入的参数是1000 就会溢出。解决的办法看下面~









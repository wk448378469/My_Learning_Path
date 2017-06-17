
class Animal(object):
    pass

#大类，动物和哺乳

class Mammal(Animal):
    pass
class Bird(Animal):
    pass

#小类，各种动物

class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#这个时候再加上Runnable 和Flyable
class Runnable(object):
    def run (self):
        print ('running...')
class Flyable(object):
    def fly(self):
        print ('flying...')

#然后把这两个加入到我们刚刚建立的N个继承的层次中

class Dog (Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
#重新定义子类的继承，告诉python现在的子类继承两个，顺序也要注意哦

#但是这样看不出继承的关系，所以用MixIn来做继承关系

#class Dog(Mammal,RunnableMixIn):     #在加上一个食肉动物！
#   pass





#定制类！！！！！！！1
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)'%self.name
print (Student('Michael'))



#类被for 循环        利用__iter__()方法！
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1   #初始化两个计数器

    def __iter__(self):
        return self          #实现本身就是迭代对象，故返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b    #计算下一个值
        if self.a>100000:            #退出循环条件
            raise StopIteration()
        return self.a

for n in Fib():
    print (n)

#用__getitem__来实现像列表那样的取元素

class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib()
print (f[0])
print(f[100])
print (list(range(100))[5:10])



class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):        #n是索引
            a,b =1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):     #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a,b = b,a+b
            return L
f = Fib2()
print (f[0:5])
print (f[:10])
print (f[:10:3])       #但是对step的参数没有做出回应


class Student1(Student):
    def __init__ (self):
        self.name = 'Michael'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
#当调用不存在的属性时，调用getattr。只有没有搜索到调用的属性时才会出现getattr

s = Student1()
print (s.score)


class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__

Chain().status.user.timeline.list
#这里不是很懂。。。




#实例也可以有自己的属性和方法
class Student4(object):
    def __init__(self,name):
        self.name = name
    def __call__ (self):
        print('My name is %s'%self.name)

#调用方法
s = Student4('Michael')
s()
#看一个函数或者一个方法是否能被调用，一个可调用的对象就是Callable对象
print (callable(Student4))
print (callable(max))
print (callable([1,2,3]))
print (callable('str'))




#使用枚举类
#当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print (name,'>=',member,',',member.value)
#value 属性自动复制给成员的int常量默认从1开始计数


from enum import Enum,unique
@unique             #装饰器检查有没有重复值i
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)
print (Weekday.Tue)
print (Weekday['Tue'])
print (Weekday.Tue.value)
print (day1 == Weekday.Mon)
print (Weekday(1))
#以上都是调用方法




#使用元类
def fn(self,name='world'):         #定义函数
    print ('Hello,%s'%name)
Hello = type('Hello',(object,),dict(hello = fn))     #创建Hello class
#type()不仅可以查看类型，还可以定义class
h = Hello()
h.hello()
print (type(Hello))
print (type(h))

#type()创建class 需要1、名称   2、继承的父类集合（注意tuple的写法，不要忘记，）        3、class的方法名称与函数绑定



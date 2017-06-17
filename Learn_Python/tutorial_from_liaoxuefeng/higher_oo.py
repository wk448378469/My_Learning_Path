
class Student (object):
    pass

s = Student()
s.name = 'wangkai' #动态给实例绑定一个属性
print (s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25)      #调用实例方法
print (s.age)
#给一个实例绑定的方法，对另一个实例是不起作用的


#给所有实例绑定方法！
def set_score(self,score):
    self.score = score
    
Student.set_score = MethodType(set_score,Student)

s2 = Student()
s2.set_score(100)
print (s2.score)

#使用__slots__
class Student1(object):
    __slots__ = ('name','age')  #用tuple定义准许绑定的属性名称

s = Student1()     #创建新实例
s.name = 'Michael'      #绑定属性‘name’
s.age = 25           #绑定数‘age’

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：



class Student2(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an insteger!')
        if value<0 or value>100:
            raise ValueError ('score must between 0~100!')
        self._score = value

s = Student2()
s.set_score(60)
print (s.get_score())


class Student3(object):
    @property                #把一个方法变成了属性
    def score(self):
        return self._score
    @score.setter               #这个装饰器负责把方法编程属性复制
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError ('score must be an integer!')
        if value <0 or value>100:
            raise ValueError ('score must between 0~100!')
        self._score = value

s = Student()
s.score = 60  #语句可执行，实际转化为 s.set_score(60)
print (s.score)


class Student4(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
#birth是可读写的属性   age则是只可读的属性
#property+setter就是可读写，没有property就是只可读！！！！！！


class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432 ,'1024*768= %d?'%s.resolution

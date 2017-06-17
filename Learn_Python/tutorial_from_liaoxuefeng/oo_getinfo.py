#获取对象信息

print (type(123))
print (type('str'))
print (type(None))
print (type(abs))


print (type(123)==type(345))
print (type(123)==int)
print (type('adv')==str)
print (type('adv')==type(123))


import types
def fn():
    pass
#基本数据类型判断用int str等   但如果要判断一个对象是否有函数要用到types模块中定义的常量
print (type(fn)==types.FunctionType)
print (type(abs)==types.BuiltinFunctionType)
print (type(lambda x:x)==types.LambdaType )
print (type((x for x in range(10)))==types.GeneratorType)
# 以上结果都是true

#类的继承关系获取信息要用isinstance！之前也有用到过

class Animal(object):
    def run (self):
        print ('run run run ...')


class Dog(Animal):
    pass
class Husky(Dog):
    pass

h = Husky()
print ('1',isinstance(h,Husky))
print ('2',isinstance(h,Dog))
print ('3',isinstance(h,Animal))


#能用type判断的也可以用isinstance判断
print (isinstance([1,2],list))
print (isinstance((1,2),(list,tuple)))       #（1,2）是list or tuple中的一种！
print (isinstance((1,2),list))



#获取一个对象的所有属性和方法，用dir()  他返回一个字符串
print (dir('asd'))

print (len('adv')==('abd'.__len__()))
#在len()函数内部，它自动去调用该对象的__len__()方法，所以他们是等价的


class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print (len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
#测试对象的属性：

print (hasattr(obj,'x'))   #有属性 ‘x’吗？
print (obj.x)
print (hasattr(obj,'y'))
setattr(obj,'y',19)   #设置一个属性‘y’
print (hasattr(obj,'y'))
print (getattr(obj,'y'))  #获取Y属性
print (obj.y)




#实例属性和类属性
class Student(object):
    def __init__(self,name):
        self.name = name

s = Student('Bob')
s.score = 90
#根据类创建的实例可以任意绑定属性。
#给实例绑定属性的方法是通过实例变量，或者通过self变量：

#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student1(object):
    name = 'Student'


class Student(object):
    name = 'Student'
s = Student()          #创建实例
print (s.name)          #d打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print (Student.name)   #打印类的name属性
s.name = 'Michael'    #给实例绑定name属性
print (s.name)         #由于实例属性优先级高于类属性，因此会屏蔽类属性
print(Student.name)    #但是类属性并没有消失，用student.name仍然可以访问
del s.name            #删除实例的name属性
print (s.name)       #再次调用s.name，由于实例的name属性没有找到，类的属性显示出来



 

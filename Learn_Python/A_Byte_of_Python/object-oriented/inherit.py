#coding=utf-8
#这个主要讲的是“继承”！当两个大的分类有共同点又有不同点的时候，抽取出他们的共同点建立一个类，然后他们分别在间隔具有各自特殊属性的类！
#子类继承总类的全部内容，再加上自己的类的特殊性就可以达到很好的修改内容的效果~
#当然不能叫做子类和总类。
#下面的代码中，SchooMember被称为基本类或超类
#而Teacher和Student则被称为导出类或者子类
class SchooMember:
    '''Represents any school member'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print 'Initialized School Member:%s'%self.name

    def tell(self):
        '''Tell my detail'''
        print 'Name:"%s" Age:"%s"'%(self.name,self.age)

class Teacher(SchooMember):                                      #继承的用法体现在这里，()中加入继承的源头
    '''Represents a teacher:'''
    def __init__(self,name,age,salary):                          #salary 工资
        SchooMember.__init__(self,name,age)                      #这句话很重要呀，应该是程序执行到这里的时候通过子类来传给基本类他所需要的内容
        self.salary=salary                                       #初始化子类的特殊内容
        print '(Initialized Teacher:%s)'%self.name

    def tell(self):
        SchooMember.tell(self)                                     #这行代码也很重要！！！
        print 'Salary:%d'%self.salary

class Student(SchooMember):
    '''Represents a student:'''
    def __init__(self,name,age,marks):                             #mark 分数
        SchooMember.__init__(self,name,age)
        self.marks=marks
        print '(Initialized Student:%s)'%self.name

    def tell(self):
        SchooMember.tell(self)
        print 'Salary:%d'%self.marks

t=Teacher('Mrs.Shrividya',40,30000)                              #用一个元组组合来定义类的名称
s=Student('Swaroop',22,75)

print

members=[t,s]                  #将两个对象组成一个列表
for member in members:
    member.tell()
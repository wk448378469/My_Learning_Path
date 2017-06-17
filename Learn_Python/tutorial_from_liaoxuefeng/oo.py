
class Student(object):          #object 是继承的类，后面再学
    pass

bart = Student()

bart.name = 'Bart Simpson'   #给实例变量绑定一个属性

class Student(object):
    def __init__(self,name,score):     #在定义的时候就把属性添加进去。__init__第一个参数永远是self
        self.name = name
        self.score = score

bart = Student('bart simpson',59)
print(bart.name)
print(bart.score)

#类的感念和函数的感念基本上没什么区别，除了第一个self。此外也可以使用默认参数、可变参数、关键字参数、命名关键字参数

def print_score(std):
    print('%s:%s'%(std.name,std.score))

print_score(bart)
#把数据处理的方法也放到类中，就是数据封装


class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s-%s '%(self.name,self.score,self.get_grade()))
    def get_grade(self):
        if self.score>=90:
            return'A'
        elif self.score>=60:
            return'B'
        else:
            return 'C'
std1 = Student('wangkai',100)
std1.print_score()

#限制访问，在属性名称前加上两个__就变成了私有变量（private），只有内部可以访问，外部不可以访问


class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s'%(self.__name,self__score))

bart = Student('Bart Simpson',97)

#这样外部就无法访问实例变量.__name 和.__score

#如果想获取的话就用get_name的方法
class Student(object):
    ...
    def get_name(self):
        return self.__name




#继承和多态！！！

class Animal(object):
    def run (self):
        print('Animal is running...')

class Dog (Animal):            #Animal 是父类，dog和cat是子类，继承自animal
    pass

class Cat (Animal):
    pass

dog = Dog()           #继承的好处就是什么都不写子类就可以全部继承父类的全部类中的内容
dog.run()
cat = Cat()
cat.run()

#子类增加些方法

class Fish(Animal):
    def run(self):
        print('Fish is running...')
    def eat(self):
        print('Eating meat...')

fish = Fish()
fish.run()
fish.eat()

#子类对父类的改进(覆盖同名的方法)（多态）

class Dog1(Animal):
    def run (self):
        print('Dog is running...')
class Cat1(Animal):
    def run (self):
        print ('Cat is running...')
dog = Dog1()
dog.run()
cat = Cat1()
cat.run()

a = list()
b = Animal()
c = Dog()

print (isinstance(a,list))
print (isinstance(b,Animal))       #类就是一个数据类型，和python本身的list本质没什么区别
print (isinstance(c,Dog))

print (isinstance(c,Animal))        #这个没什么的，就是子类的数据类型也是父类的数据类型

def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(Animal())
run_twice(Dog1())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())
#好处在于，当我们为Animal增加一个子类的时候，不需要对run_twice做什么修改。直接调用就可以



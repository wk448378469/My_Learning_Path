
#for 循环的数据类型
#1、list、tuple、dict、set、str
#2、generator（包含生成器和带yield的function）

#可以被for循环的对象统称为可迭代对象：Iterable。可以用isinstance()检测

from collections import Iterable

print (isinstance([],Iterable))     #T
print (isinstance((),Iterable))     #T
print (isinstance({},Iterable))     #T
print (isinstance('a',Iterable))    #T
print (isinstance((x for x in range(10)),Iterable))     #T
print (isinstance(100,Iterable))    #F


#可以被next()函数调用并不断返回下一个值的对象成为“迭代器”！！

#可以使用isinstance()判断一个对象是否是Iterator对象：

from collections import Iterator
print (isinstance((x for x in range(10)),Iterator))   #T
print (isinstance([],Iterator))                     #F
print (isinstance({},Iterator))                     #F
print (isinstance('asd',Iterator))                  #F


#list、ditc、str虽然是Iterable,但不是Iterator
#要是想变成Iterator 需要调用函数：iter()


print (isinstance(iter([]),Iterator))
print (isinstance(iter('asd'),Iterator))



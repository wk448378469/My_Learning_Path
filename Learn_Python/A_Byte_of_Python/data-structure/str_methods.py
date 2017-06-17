#coding=utf-8
#字符串也是对象，python中一切皆对象！

name='Swaroop'   #This is a string object

if name.startswith('Swa'):
    print 'Yes,the string startswith"Swa"'

if 'a'in name:
    print 'Yes,it contains the string"a"'

if name.find('war')!=-1:
    print 'Yes,it contains the string"war"'

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print delimiter.join(mylist)

#最有一个是把分隔符加入到列表中，返回一个更大的字符串
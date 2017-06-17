
#无限的的迭代器

#import itertools
#natuals = itertools.count(1)
#for n in natuals:
#    print (n)


#cycle循环一个序列无限的。。
#import itertools
#cs = itertools.cycle('abc')
#for c in cs:
#    print (c)


#repeat() 一个元素无限循环,提供第二个参数就有限循环
#import itertools
#ns = itertools.repeat('a',3)
#for n in ns:
#    print (n)



#无限数列截取有限数列
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
for n in ns:
    print (n)


#一组迭代对象串联起，形成更大的迭代器
for c in itertools.chain('abc','xyz'):
    print (c)


#把迭代器中相关联的元素跳出来，在一起
for key,group in itertools.groupby('asdasdaassddd'):
    print (key,list(group))
#只作用于相邻的一样的字符有效！！！


#识别大小写！
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print (key,list(group))







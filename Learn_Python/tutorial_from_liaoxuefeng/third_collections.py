#集合类

#用namedtuple来定义个tuple的对象
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print (p.x)
print (p.y)
#自己定义一种数据类型，具有tuple的不变性能，又可以根据属性查询

print (isinstance (p,Point))
print (isinstance (p,tuple))



#高效的对列表进行插入和删除
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print (q)



#defaultdict 列表缺省默认值
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1']='abc'
print (dd['key1'])
print (dd['key2'])



#dict保持key的顺序（原无序）  OrderedDict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print (d)

od = OrderedDict([('a',1),('b',2),('c',3)])
print (od)          #ordereddict 是你在输入的是时候‘定义’的顺序，并不是按照字母顺序排列

od = OrderedDict()
od['z']=1
od['y']=2
od['x']=3
x=list(od.keys())
print (x)


#简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print (c)
#Courter 是一个dict的子类，key是我们可以遍历的，值是数的次数







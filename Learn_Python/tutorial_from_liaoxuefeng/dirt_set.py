d = {'bob':95,'kk':75,'xiaoming':66}
print (d['bob'])


d['kk'] = 77
print (d['kk'])

d['kk'] = 78
d['kk'] = 79
print (d['kk'])

if 'HOHO' in d:
    print ('HOHO in d')
else:
    print ('HOHO isn\'t in d')

if d.get('HOHO'):
    print ('HOHO in d')
else:
    print ('HOHO isn\'t in d')

d.pop('kk')                  #删除key以及对应的值
print (d)

#list 查询速度慢，但占用内存少
#dict 查询速度款，但占用内存多

#dict 中 key不可变！


s = set([1,2,3])
print (s)

#set和dict类似，但是只是一组key的集合，但不存储value。要创建一个set，需要提供一个list作为输入集合

s = set ([1,1,1,1,52,2,2,2,12,2,3,2,2])
print (s)

s.add(4)
s.add(4)
print (s)

s.add(4)
print (s)
print (len(s))

s.remove(1)
print (s)

s1 = set ([1,2,3])
s2 = set ([2,3,4])
print (s1&s2)
print (s1|s2)

a = ['c','b','a']
a.sort()
print (a)

a ='abc'
a.replace('a','A')
print (a)          #没替换成功
b = a.replace('a','A')
print (b)           #替换成功

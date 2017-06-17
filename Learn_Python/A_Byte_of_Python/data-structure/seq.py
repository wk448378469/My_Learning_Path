#coding=utf-8

#序列、元组、字典都是序列
#seq是序列的英文缩写？

shoplist=['apple','mango','carrot','banner']
#Indexing or 'Subscription' operation  这个注释需要去翻译一下      翻译结果：索引或订阅操作

print 'Item 0 is',shoplist[0]
print 'Item 1 is',shoplist[1]
print 'Item 2 is',shoplist[2]
print 'Item 3 is',shoplist[3]
print 'Item -1 is',shoplist[-1]
print 'Item -2 is',shoplist[-2]

#Slicing on a list   还是需要翻译一下，感觉自己的英文好弱！！！         翻译结果：切割清单
print 'Item 1 to 3',shoplist[1:3]
print 'Item 2 to end is',shoplist[2:]
print 'Item 1 to -1 is',shoplist[1:-1]
print 'Item start to end is ',shoplist[:]

#Slicing on a string
name='swaroop'
print 'characters 1 to 3 is',name[1:3]
print 'characters 2 to end is',name[2:]
print 'characters 1 to -1 is',name[1:-1]
print 'characters start to end is',name[:]

#字符串可以索引位置信息，也可以索引字典、列表、和元组的内容！！！需要使用切片操作符[:]
#-1是指倒数第一个项目的信息！！！





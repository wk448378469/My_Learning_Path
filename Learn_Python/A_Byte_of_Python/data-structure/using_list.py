#coding=utf-8
#This is my shopping list
shoplist=['apple','mango','carrot','banana']                     #建立一个列表，格式是['对象1','对象2']

print 'I have',len(shoplist),'items to purchase.'               #len()用来统计列表中的对象数量

print 'These items are:'
for item in shoplist:                                               #循环，利用一个变量循环获取列表中各项目的值
    print item

print '\n I also have to buy rice.'
shoplist.append('race')                                             #利用append()在列表的尾部添加一个对象
print 'My shopping list is now',shoplist

print 'I will sort my list now'
shoplist.sort()                                                       #sort()给列表进行按首字母排序
print 'Sorted shopping list is',shoplist

print 'The first item I will buy is ',shoplist[0]               #记住python是从0开始计数的！！！
olditem=shoplist[0]
del shoplist[0]                                                      #删除列表中特定序号的对象

print 'I bought the',olditem
print 'My shopping list is now',shoplist
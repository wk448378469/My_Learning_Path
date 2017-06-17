#coding=utf-8

#referece 是引用的意思

print 'Simple A ssignment'
shoplist=['apple','mango','carrot','banner']
mylist=shoplist        #mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist
#notice that both shoplist and mylist both print the same list with out
#the 'apple'confirming that they point to the same object

print 'Copy by making a full slice'
mylist=shoplist[:] #make a copy by doing a full slice           full slice全切

del mylist[0] #remove first item

print 'shoplist is ',shoplist
print 'mylist is',mylist
#notice that now the two lists are different
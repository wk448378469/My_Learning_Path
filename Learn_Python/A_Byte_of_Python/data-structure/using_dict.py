#coding=utf-8

ab={
    'Swaroop':'Swaroop@byteofpython.info',
    'larry':'larry@wall.org',
    'Mastumoto':'mazt@ruby-lang.org',
    'Spammer':'spammer@homail.com',
}

print "Swaroop's address is %s"%ab['Swaroop']

#adding a key/value pair
ab['Guido']='guido@python.org'

#delete a key/value pair
del ab['Spammer']

print '\n There are %d contact in the address-book \n'%len(ab)
for name,addrees in ab.items():
    print 'Contact %s at %s '%(name,addrees)

if'Guido'in ab:   #or ab.has_key('Guido')
    print "\n Guido's address is %s"%ab['Guido']

#字典就像是我们的通讯录，可以这样去理解方便记忆。也可以使用ad和del来增加很删除字典中的项目，每个项目需要一个key（键）/value(值)。在print中索引相应的key就可以
#打印key对应的值了

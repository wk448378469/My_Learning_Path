#coding=utf-8

import cPickle as p                       #调用一个模块，模块的作用是在文件中储存任何一个python的对象，并且简化他的名称！！！！
#另外一个模块Pickle也一样，不过cPickle是用C语言写的，速度快得多！

shoplistfile='shoplist.data'       #the name of the file where we will store the object

shoplist=['apple','mango','carrot']

#write to file

f=file(shoplistfile,'w')
p.dump(shoplist,f)               #dump the object to a file。把对象存到打开的文件中
f.close()

del shoplist            #remove the shoplist

#read back from the storage
f=file(shoplistfile)
storedlist=p.load(f)           #用load函数的返回来取回对象！
print storedlist



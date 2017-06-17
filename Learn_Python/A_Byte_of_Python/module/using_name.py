#Filename:using_name.py

if __name__=='__main__':
#注意！！！！这里调用的模块是两个下划线！！！！！！__name__是查询模块的名字。此外模块的名称是模块的第一个参数
    print 'This program is being run by itself'

else:
    print 'I am being imported from another module'
#-*- coding:utf-8 -*-

'a test module'

__author__ = 'wangkai'
                         #这之前都是标准模板
import sys                                  #导入模块

def test():                                 #argv是用list存储了命令行的所有参数，至少有一个，因为第一个参数都是该文件名.py    
    args = sys.argv
    if len(args)==1:
        print('Hello,world')
    elif len(args)==2:
        print ('Hello,%s!'%args[1])
    else:
        print ('Too many argumens!')

if __name__ == '__main__':
    test()


#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
    

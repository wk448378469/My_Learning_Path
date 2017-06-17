# coding=utf-8

import sys
#告诉程序我们要调用sys这个模块了，sys模块包含了与python解释器和它工作环境有关的函数。

print 'The command line arguments are:'
#The command line arguments are的意思是命令行列表

for i in sys.argv:
#sys.argv是变量，其次他是一个字符串的列表（后面会讲到）

    print i,'\n'

print 'The PYTHON PATH is',sys.path,'\n'

#这一块有点没懂，不要紧先过去再说
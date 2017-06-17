#coding=utf-8

import sys
dir(sys)
[
    '__displayhook__','__doc__','__excepthook__','__name__',
    '__stderr__','__stdin__','_getframe','api_version','argv',
    'builtin_module_names','byteorder','call_tracing','callstats',
    'copyright','displayhook','exc_clear','exc_info','exc_type','excepthook',
    'exec_prefix','execcutable','exit','getcheckinterval','getdefaultencoding',
    'getdlopenflags','getfilesystem encoding'

]
dir()
['__builtins__','__doc__','__name__','sys']
a=5
dir()
['__builtins__','__doc__','__name__','a','sys']
print dir()

del a
dir()
['__builtins__','__doc__','__name__','sys']

print dir()

#dir是内建函数列出模块定义的标识符（函数、类、变量）。。。其实这里还是有点不明白  9 9
#del 语句是删除当前模块中的变量/属性

#dir()      不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
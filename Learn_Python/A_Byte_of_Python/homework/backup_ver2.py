#coding=utf-8
#百度查一下，已经保存到文件夹中了，明天看看
import os
import time

source=['C:\\Data']
target_dir='D:\\text\\'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today
    #检测在备份中是否有当前日期作为名称的目录，如果用os.mkdir()函数来创建

target=today+os.sep+now+'.7z'
zip_command = "7z a %s %s" %(target,' '.join(source))
if os.system(zip_command)==0:
    print 'Successful back up',target
else:
    print 'Backup FAILED'



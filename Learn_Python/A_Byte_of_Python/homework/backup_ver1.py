#coding=utf-8
import os
import time

#1.文件和目录可以backde起来在list.as指定
source=[r'C:\\data',r'D:\\test']

#2.备份必须存储在主备份目录中
target_dir='\\nt\\e\\backup\\'
#3.Remember to change this to what you will be using

#压缩档案的名称是当前日期和时间
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.rar'

#5.我们使用zip命令（在Unix / Linux）放在一个ZIP档案文件
rar_command="rar a'%s'%s"%(target,''.join(source))

#运行备份
if os.system(rar_command)==0:
    print 'Successful back up to',target
else:
    print 'Back up FAILED'

#版本一的失败了，找了半天原因也找不出来为什么会有乱码的情况9 9 9 9 9 9 9 9 9 9 9 9 9  9 9 9 9
#简明python中是用zip作为解压工具的，没有zip 所以尝试用rar9 9  结果还是不要是呀，臣妾太心塞了！！！
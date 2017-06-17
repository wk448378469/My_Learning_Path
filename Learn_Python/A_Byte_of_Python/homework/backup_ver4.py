#coding=utf-8
#程序的目标选定一个文件夹，然后将它压缩到特定的目录中来，然后这个压缩包按照特定的名称来命名。基本上就这样，做了好几天昨天上午才开始正式的跑通，会在小面的注释中一次提到遇到的问题

import os
import time
#这里是调用两个模块，os和time。os是系统操作模块，主要用来处理文件和目录这些我们日常手动需要做的操作。其中下面用到的两个函数分别是
#os.sep和os.mkdir()、还有一个！！！！os.path.exists()这三个。os.sep主要用于系统路径中的分隔符，Windows系统通过是“\\”，Linux类系统如Ubuntu的分隔符是“/”，而苹果Mac OS系统中是“:”。
#os.mkdir() 是创建目录的意思。。。此外os模块也是python标准库中的比较好的跨平台模块所以要多多学习哦
#还有就是出了上面用到的三个还有些
#1 )os.path.exists()是检验括号中的路径是否存在的!!!!!
#2 )、os.getcwd()获取当前路径，这个在Python代码中比较常用。
#3 )、os.listdir() 列出当前目录下的所有文件和文件夹。
#4 )、os.remove() 方法可以删除指定的文件。
#5 )、os.system() 方法用来运行shell命令。
#6 )、os.chdir() 改变当前目录，到指定目录中。

#另外一个模块是time
#主要是提供各种操作时间的函数（我们用时间来命名备份后的文件和目录），我们在下面的程序中用到了time模块中的time.strftime()函数。函数的作用是将制定的struct_time
#(默认为当前时间)，根据制定的格式化字符串输出
#除此之外time模块中也有其它的函数，简单列举几个
#1.asctime()    asctime([tuple]) -> string将一个struct_time(默认为当时时间)，转换成字符串
#2.clock() clock() -> floating point number该函数有两个功能， 在第一次调用的时候，返回的是程序运行的实际时间；以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
#3.ctime(...)  ctime(seconds) -> string将一个时间戳(默认为当前时间)转换成一个时间字符串
#4.mktime(...)   mktime(tuple) -> floating point number   将一个以struct_time转换为时间戳
#5.strptime(...)   strptime(string, format) -> struct_time  将时间字符串根据指定的格式化符转换成数组形式的时间

source = ['C:\\Data']       #源文件的目录！这里要注意的是在Win下一定要是两个"\"    并且这个源文件一定要存在！
target_dir = 'D:\\text\\'    #备份的目标目录定义，和上面那条语句一样！两个\   和一定要存在
today=target_dir+time.strftime('%Y%m%d')          #定义一个时间变量，由目标目录和年月日时间字符串（由函数来获取）组成
now=time.strftime('%H%M%S')                       #定义当下的时间，由函数获取当下的时分秒时间，并转为字符串
comment=raw_input('Enter a comment:')           #comment的含义是注释、评论。输入一个备份的备注

if len(comment)==0:                                 #判断一下comment的长度是否为0
    target=today+os.sep+now+'.7z'                   #如果为0则定义目标文件名称的时候不需要添加comment字段
else:
    target=today+os.sep+now+'_'+comment.replace('','_')+'.7z'      #如果不为0则定义目标文件名称的时候加入了comment字段并且，用了replace函数来替换格式！！语法：str.replace(old, new[, max])  max是可选字符串长度不超过的意思
                                                                      #此外，os.sep这个os模块中的语句帮我们把一个字符串变成了当前系统下的目录
if not os.path.exists(today):                               #如果today的这个路径不存在
    os.mkdir(today)                                                 #创建today的目录
    print 'Successfully created directory',today              #打印成功

zip_command = "7z a %s %s" %(target,' '.join(source))            #使用7z命令来压缩文件   a是add  后面还用到了join函数把source列表转化为字符串
                                                            #这里还用到了一个知识点就是把target、source组成一个元组
if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup FAILED'

#最后埋的坑之一是电脑没装zip
#之二十电脑装了zip，但是在电脑的系统变量中的path设置为zip 的安装目录
#之三就是zip收费~后来换成了7zip
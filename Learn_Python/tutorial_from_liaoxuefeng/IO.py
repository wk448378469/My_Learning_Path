
#三种打开文件，和关闭文件的方法
f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','r')
print (f.read())
f.close()   #记得关闭文件，因为内存有限

try:
    f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','r')
    print (f.read())
finally:
    if f:
        f.close()
        
with open ('C:/Users/Administrator/Desktop/新建文本文档.txt','r') as f:
    print (f.read())


#读取特定数量的内容
f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','r')
for line in f.readlines():
    print (line.strip())       #把末尾的‘回车换行’删掉


#其它的文件读取方式
#二进制文件(通常是读取图片和视频等)
f = open ('C:/Users/Administrator/Desktop/新建文本文档.txt','rb')
print (f.read())
f.close()


#字符编码
f = open ('C:/Users/Administrator/Desktop/新建文本文档.txt','r',encoding='gbk')
print (f.read())
f.close()

#处理异常（通常是忽略）
f = open ('C:/Users/Administrator/Desktop/新建文本文档.txt','r',encoding='gbk',errors='ignore')
print (f.read())
f.close()






#写文件！

f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','w')
f.write('吾皇驾到')
f.close
f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','r')
print (f.read())
f.close


#用with语句来保障不忘记关闭文档
with open ('C:/Users/Administrator/Desktop/新建文本文档.txt','w') as f:
    f.write('Hello,word!')
f = open('C:/Users/Administrator/Desktop/新建文本文档.txt','r')
print (f.read())
f.close

from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')
print (f.getvalue())
#写到内存里


from io import StringIO
f = StringIO('Hello!\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print (s.strip())


from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print (f.getvalue())

import os
print (os.name) #打印系统操作类型，nt是win

print (os.environ) #打印操作系统中的环境变量

print (os.environ.get('path'))  #单一某个环境变量的值


#操作文件和目录
os.path.abspath('.') #查看当前目录的绝对路径
os.path.join('\\Users\\Administrator\\PycharmProjects\\廖雪峰的教程(3.X的)','testdir')
#在某个目录下创建一个新目录，但是这步并没有创建目录，作用是显示出加上新目录之后的完整路径
#利用os.path.join()的好处在于python会根据系统自动处理不同系统的路径分隔符

os.mkdir('\\Users\\Administrator\\PycharmProjects\\廖雪峰的教程(3.X的)\\testdir')
#创建一个新目录，这一步才添加成功
os.rmdir('\\Users\\Administrator\\PycharmProjects\\廖雪峰的教程(3.X的)\\testdir')
#删除一个目录！


#拆分路径的函数
os.path.split('\\Users\\Administrator\\PycharmProjects\\廖雪峰的教程(3.X的)\\oo.py')

#得到文件扩充名
os.path.splitext('\\Users\\Administrator\\PycharmProjects\\廖雪峰的教程(3.X的)\\oo.py')

#os.rename('text.txt','text.py')
#当前目录下文件重命名

#os.remove('text.py')
#删除文件当前目录下

#查看当前目录下所有的目录
print ([x for x in os.listdir('\\Users') if os.path.isdir(x)])

#列出所有.py文件
print ([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
#os.path.isfile() 检查对象是不是file








#序列化
import pickle
d = dict(name='bob',age=20,score=88)
print (pickle.dumps(d))          #把对象序列化并写入文件

#pickle.dumps() 和pickle.dump()两种方法把对象序列化成bytes，然后写入文件
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close

f = open('dump.txt','rb')
d = pickle.load(f)        #在反序列化的读出来
f.close
print (d)



#用JSON数据格式作为传递对象在不同语言中
#将python中的数据格式转为JSON格式

import json
d = dict(name='bob',age=20,score=99)
print (json.dumps(d))

#dumps()是返回一个str，内容是标准的JSON，dump()就是写入到文件中
#loads()是把JSON反序列化                 load()就是读取文件中的JSON并反序列化
json_str='{"age":20,"score":99,"name":"hahaha"}'
print (json.loads(json_str))


#python中的class转化为JSON
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('wangkai',25,100)

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score,
        }

print (json.dumps(s,default=student2dict))
#如果还有一个Teacher的class的话我们就可以稍微偷个懒用lambda
#print (json.dumps(s,default=lambda obj:obj.__dict__))

       

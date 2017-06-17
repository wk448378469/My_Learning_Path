s ='abc\\-001'   #python的字符串
                 #正则表达式字符串：'abc\-001'

#因为python中有转移符\

#所以最好的定义方式是

s = r'abc\-001'
#即r+正则表达式的字符串




#正则的判断
import re
print (re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print (re.match(r'^\d{3}\-\d{3,8}$','010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print ('ok')
else:
    print ('failed')



#用正则表达式切分字符串
print ('a  b    c'.split(' '))
print (re.split(r'\s+','a b   c'))
print (re.split(r'[\s\,]+','a  ,b   ,c ,d'))
print (re.split(r'[\s\,\:]+','a,f    ,:c,     e'))




#利用正则表达式分组字符串
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print (m)
print (m.group(0))
print (m.group(1))
print (m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print (m.groups())




#正则匹配的贪婪匹配——?
print (re.match(r'^(\d+)(0*)$','1023000').groups())
print (re.match(r'^(\d+?)(0*)$','1023000').groups())




#正则表达式的复用
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print (re_telephone.match('010-12345').groups())
print (re_telephone.match('010-8086').groups())



#练习
import re
while True:
    email = input('please enter a email address:')
    re_email = re.compile(r'^([0-9a-zA-Z]+)?@([a-z]+)(.org|.com)$')
    res = re.match(re_email,email)
    if res:
        print ('ok')
    else:
        print ('sorry')
        
    

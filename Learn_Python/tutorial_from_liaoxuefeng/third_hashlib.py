#数据加密，摘要算法（哈希算法，散列算法）
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print (md5.hexdigest())



#字符串较长可以分批次的update
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())



#另外一种摘要算法SHA1
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print (sha1.hexdigest())


#注册
db = {}
input('欢迎来到python world!请注册...')
username = input('请输入用户名:')
password = input('请输入密码:')

def get_md5(password):
    psdmd5=hashlib.md5()
    psdmd5.update(password.encode('utf-8'))
    return psdmd5.hexdigest()

def register ():
    db[username] = get_md5(password+username+'the-Salt')
    print ('注册成功!')
    
register()
#登录
username1 = input('您的用户名:')
password1 = input('您的密码:')

def login():
    if username1 in db:
        if db[username] == get_md5(password1+username+'the-Salt'):
            print ('登录成功！')
        else:
            print ('亲，密码错误')
    else:
        print ('亲,用户名错误')
login()

print (db)

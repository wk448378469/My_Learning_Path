from wsgiref.simple_server import make_server
from Hello import application

#创建一个服务器，IP地址为空，端口9000，处理海曙是application
httpd = make_server('',9000,application)
print ('Serving HTTP on port 9000...')

#开始监听Http的请求
httpd.serve_forever()


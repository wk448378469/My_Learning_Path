
#web应用，wsgi处理函数

def application(environ,start_response):
    start_response('200K', [('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']



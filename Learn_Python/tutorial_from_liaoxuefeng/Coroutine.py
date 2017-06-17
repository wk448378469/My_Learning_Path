def consumer():
	r = ''
	while True:     
		n=yield r  
		#如果是produce调用send的话，就相当于在consumer中为n赋值
		#如果是consume调用yield r的话，就相当于在produce中为r赋值
		if not n: 
			return
		print ('[CONSUMER] Consuming %s...'%n)
		r='200k'

def pronduce(c):
	c.send(None)
	n=0
	while  n<5:
		n=n+1
		print ('[PRODUCER] Producing %s...'%n)
		r=c.send(n)
		print ('[PRODUCER] Consumer return:%s'%r)
	c.close()
c=consumer()
pronduce(c)



import asyncio
@asyncio.coroutine
def hello():
	print ('Hello world!')
	#异步调用asyncio.sleep
	r=yield from asyncio.sleep(1)
	print ('Hello again')

#获取Eventloop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()




import threading
import asyncio

@asyncio.coroutine
def hello():
	print ('Hello world! (%s)'%threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again!(%s)'%threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
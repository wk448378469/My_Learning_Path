

try:
    print ('try...')
    r = 10/0
    print ('result:',r)

except ZeroDivisionError as e:
    print ('except:',e)

finally:
    print ('finally...')
print('END')
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。


try:
    print ('try...')
    r = 10/2
    print ('result:',r)
except ZeroDivisionError as e:
    print ('except:',e)
finally:
    print ('finally...')
print ('END')
#由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。



try:
    print ('try...')
    r = 10/int('a')
    print ('result:',r)
except ValueError as e:
    print ('ValueError:',e)
except ZeroDivisionError as e:
    print ('ZeroDivisionError:',e)
finally:
    print ('finally...')
print ('END')



try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')



#记录错误,而且程序不会因为错误而打断
import logging
def foo(s):
    return 10/int(s)
def bar (s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('end')




#抛出错误(错误也是class)
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s'%s)
    return 10/n
#foo('0')


import pdb
s = '0'
n = int(s)
pdb.set_trace()   #打断点！
print (10/n)

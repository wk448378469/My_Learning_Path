print (abs(100))
print (abs(-100))

print(max(1,2,2,3,1,4,5,1,5,12,123))


print (int('123'))
print (int(12.4))
print (float('123.45'))
print (str(123.4))
print (bool(1))
print (bool(''))       #数据类型转换之。。。你懂的就是真假


a = abs
print(a(-1))            #函数名指向一个函数对象的引用，其实就是起了一个花名


n1 = 255
n2 = 1000
print (hex(n1))
print (hex(n2))            #hex()把一个整数转为十六进制的字符串

def my_abs(x):
    if x>0:
        return x
    else:
        return -x


print (my_abs(-1))


'''def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')              #错误和异常处理
    if x>0:
        return x
    else:
        return -x


test = input('please enter a number:')     
print (my_abs2(test))
'''

import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)    #感觉上是返回两个值，只是表象。
r = move(100,100,60,math.pi/6)      #对比上面的语句看打印的结果就会发现，其实python返回的是一个元组tuple。
print (x,y)
print (r)                           #在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。




import math
'''def quadratic(a,b,c):
    if a not 0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a*b)
        x2 = (-b+math.sqrt(b*b-4*a*c))/(2*a*b)
        return x1,x2
    elif b ==0:
        x1 = -c/b
        x2 = x1
        return x1,x2
    else:
        return 你脑残！
x = input('please enter a number for a:')
y = input('please enter a number for b:')
z = input('please enter a number for c:')

print ('x1=:',quadratic(x,y,z))
print ('x2=:',quadratic(x,y,z))
'''

def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)) :
        print ('程序错误')
        return None
    gen = b*b-4*a*c
    if gen<0:
        print ('此方程无解！')
        return None
    elif a==0:
        print ('此方程的解：')
        return -b/c
    else :
        print ('此方程的解：')
        return (-b+math.sqrt(gen))/2*a*b,(-b-math.sqrt(gen))/2*a*b

x = float(input('please enter a number for a:'))
y = float(input('please enter a number for b:'))
z = float(input('please enter a number for c:'))

print (quadratic(x,y,z))

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:03:34 2017

@author: kaifeng
"""

import numpy as np
np.version.full_version

a = np.array([0,1,2,3,4,5])
a.ndim
a.shape

b = a.reshape((3,2))
b.ndim
b.shape

b[0][1] = 27
a
b

c = a.reshape((3,2)).copy()        # 创建副本
c[0][0] = -99
c

a > 4
a[a>4]
a.clip(0,4)         # 把数组里面值得区间只能在0,4 如果不在就统一掉

c = np.array([1,2,np.nan,3,4])
np.isnan(c)
c[~np.isnan(c)]            # 这个~是什么鬼！！！，返回的结果是去除掉了nan
np.mean(c[~np.isnan(c)])

import scipy as sp
sp.version.full_version
sp.dot is np.dot             # np 和 sp  互通的？


data = sp.genfromtxt('C:/Users/carne/Desktop/web_traffic.tsv',delimiter = '\t')
print (data[:10])
print (data.shape)

X = data[:,0]
Y = data[:,1]

sp.sum(sp.isnan(Y))

X = X[~sp.isnan(Y)]
Y = Y[~sp.isnan(Y)]             # ~ 这个是个神奇的语法。。。反正就是把nan值去掉了

import matplotlib.pyplot as plt
import seaborn as sb
plt.scatter(X,Y)
plt.title('web traffic over the last month')
plt.xlabel('time')
plt.ylabel('hits/hour')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

def error(f,x,y):
    # 误差函数
    return sp.sum((f(x)-y)**2)


fp1 , residuals , rank ,sv ,rcond = sp.polyfit(X,Y,1,full=True)
# 上面这句，代表的意思是从X,Y这两个输入中，模拟出来一个直线，阶为1，误差最小....
# fp1 是y = kx + b   因为是一阶的， k = 2.59619213   b = 989.02487106
# residuals  残差   

f1 = sp.poly1d(fp1)         # 根据fp1 创建一个模型，其实就是上面y=kx+b的
error(f1,X,Y)               #总误差有点大啊....

fx = sp.linspace(0,X[-1],1000)
plt.scatter(X,Y)
plt.plot(fx,f1(fx),linewidth = 4)
plt.legend(['d =%i' % f1.order],loc = 'upper left')
plt.title('web traffic over the last month')
plt.xlabel('time')
plt.ylabel('hits/hour')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()


# 好像一阶的不是很好，换成二阶的

f2p = sp.polyfit(X,Y,2)
f2 = sp.poly1d(f2p)
# 第二个模型是二阶的， f = a1*x^2 + a2 * x + b      其中a1 = 1.05322215e-02  a2 =-5.26545650e+00  b=1.97476082e+03
error(f2,X,Y)      # 误差是一阶的一半吧
error(f1,X,Y)

fx = sp.linspace(0,X[-1],1000)
plt.scatter(X,Y)
plt.plot(fx,f1(fx),linewidth = 4)
plt.plot(fx,f2(fx),linewidth = 4)
plt.legend(['d =%i' % f1.order],loc = 'upper left')
plt.title('web traffic over the last month')
plt.xlabel('time')
plt.ylabel('hits/hour')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()


# 实验一下10阶的~~~~
f10p = sp.polyfit(X,Y,10)
f10 = sp.poly1d(f10p)
fx = sp.linspace(0,X[-1],1000)
plt.scatter(X,Y)
plt.plot(fx,f1(fx),linewidth = 4)
plt.plot(fx,f2(fx),linewidth = 4)
plt.plot(fx,f10(fx),linewidth = 4)
plt.legend(['d =%i' % f1.order],loc = 'upper left')
plt.title('web traffic over the last month')
plt.xlabel('time')
plt.ylabel('hits/hour')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

# 貌似越来越好，但是当是10阶的时候是不是有点过拟合了~
# 过拟合
# 过拟合~

#分割数据集
inflection = 3.5*7*24          #计算一下第三周和第四周的小时点
XA = X[:inflection]
YA = Y[:inflection]
XB = X[inflection:]
YB = Y[inflection:]

fa = sp.poly1d(sp.polyfit(XA,YA,1))    #重新生成模型
fb = sp.poly1d(sp.polyfit(XB,YB,1))

fa_error = error(fa,XA,YA)
fb_error = error(fb,XB,YB)

fx = sp.linspace(0,X[-1],1000)
plt.scatter(X,Y)
plt.plot(XA,fa(XA),linewidth = 4,color = 'y')
plt.plot(XB,fb(XB),linewidth = 4,color = 'r')
plt.title('web traffic over the last month')
plt.xlabel('time')
plt.ylabel('hits/hour')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

print (fa_error + fb_error)

# 貌似还是二阶的好点







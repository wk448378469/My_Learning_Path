# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:04:16 2017

@author: kaifeng
"""

import numpy as np
import pandas as pd 
import scipy.stats as stats
from math import *
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

x = np.arange(1,101)
x = np.array([float(i) for i in x])
y = x + [10*sin(0.3*i) for i in x]+stats.norm.rvs(size = 100,loc = 0,scale = 1.5)

plt.figure(figsize = (12,6))
plt.scatter(x,y)

# 训练普通模型
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
'''
    slope——斜率
    intercept——截距
    r_value——相关性系数
    p_value——是统计学中的什么概念？显著性？
    std_err——标准误差
'''

plt.figure(figsize = (12,6))
yHatLinear = intercept + slope*x
plt.plot(x,yHatLinear,'r')
plt.scatter(x,y)

# 权重
def get_sqrW(x0,k):      # x0处其他样本的点的权重
    w = np.zeros(len(x))
    for i in range(len(x)):
        w[i] = exp(-(x[i]-x0)**2/(2*k*k)) # k是波长函数
    w = np.array([sqrt(i) for i in w])
    return w

def get_yHat2(k):
    yHat2 = np.zeros(len(x))
    for i in range(len(x)):
        w = get_sqrW(x[i],k)
        x2 = w*x
        x2 = x2[x2>0] #去掉权重为0的样本
        y2 = w*y
        y2 = y2[y2>0]
        X = np.zeros((1,len(x2)))
        X[0] = x2
        X = X.T
        X = sm.add_constant(X,has_constant='skip')
        X[:,0] = w[w>0]
        Y = y2
        model = sm.OLS(Y,X)
        result = model.fit()
        a = result.params[0]
        b = result.params[1]
        yHat2[i] = a + b*x[i]
    return yHat2

yHat2 = get_yHat2(100000) # 当波长函数的值很大时，近似于线性回归
plt.figure(figsize=(12,6))
plt.plot(x,yHat2,'r')
#plt.plot(x,yHatLinear,'g')
plt.scatter(x,y)

yHat3 = get_yHat2(10)
plt.figure(figsize=(12,6))
plt.plot(x,yHat3,'r^')
plt.plot(x,yHatLinear,'g')
plt.scatter(x,y)

yHat4 = get_yHat2(5)
plt.figure(figsize=(12,6))
plt.plot(x,yHat4,'r^')
plt.plot(x,yHatLinear,'g')
plt.scatter(x,y)

yHat5 = get_yHat2(1)
plt.figure(figsize=(12,6))
plt.plot(x,yHat5,'r^')
plt.plot(x,yHatLinear,'g')
plt.scatter(x,y)

yHat6 = get_yHat2(0.1)
plt.figure(figsize=(12,6))
plt.plot(x,yHat6,'r^')
plt.plot(x,yHatLinear,'g')
plt.scatter(x,y)
# 这样子就太过拟合了~~~


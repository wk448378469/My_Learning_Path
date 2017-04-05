# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:19:31 2017

@author: kaifeng
"""

from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.cross_validation import KFold

boston = load_boston()

plt.scatter(boston.data[:,5],boston.target,color = 'r')

boston.DESCR

# 从一元的开始，-RM  average number of rooms per dwelling  平均房间数对价格的

x = boston.data[:,5]
x = np.array([[v,1] for v in x])         # 转行成N行一列
y = boston.target

(slope,bias),total_error,_,_ = np.linalg.lstsq(x,y)
#这个是函数可以返回很多结果，如果不要的话就用_来站位就可以
# slope 斜率   bias是什么呢？

rmse = np.sqrt(total_error[0]/len(x))
#上面返回的是总误差，求一下平均比较好理解


#尝试多个输入
x = boston.data
x = np.array([np.concatenate((v,[1])) for v in boston.data])
y = boston.target
s,total_error,_,_ = np.linalg.lstsq(x,y)
rmse = np.sqrt(total_error[0]/len(x))    # 已经变成了4.7左右了~


#换一个模型
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(x,y)

p = np.array([lr.predict(xi) for xi in x])
e = p - y

total_error = np.dot(e,e)
rmse_train = np.sqrt(total_error/len(p))      #好像有点大啊...

#弄成10折交叉运算
kf = KFold(len(x), n_folds=10)

#使用惩罚项
from sklearn.linear_model import ElasticNet
en = ElasticNet(fit_intercept=True,alpha=0.5)
en.fit(x,y)
p = np.array(map(en.predict, y))


#

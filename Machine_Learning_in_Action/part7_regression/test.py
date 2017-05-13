# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:07:29 2017

@author: 凯风
"""

import regression
from numpy import *
from imp import reload
import matplotlib.pyplot as plt

reload(regression)
xArr,yArr = regression.loadDataSet('ex0.txt')
xArr[0:2]
ws = regression.standRegres(xArr,yArr)  # 求回归系数
ws

xMat = mat(xArr)
yMat = mat(yArr)
yHat = xMat*ws      # 拟合曲线

# 绘制拟合直线和散点图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy * ws
ax.plot(xCopy[:,1],yHat)
plt.show()


# 判断模型效果
yHat = xMat * ws
corrcoef(yHat.T,yMat)       # 看[0,1]和[1,0]位置，因为自己和自己相关性肯定是1

        
# 测试局部加权线性回归
reload(regression)
xArr,yArr = regression.loadDataSet('ex0.txt')
regression.lwlr(xArr[0],xArr,yArr,1.0)  # 单点测试
regression.lwlr(xArr[0],xArr,yArr,0.001)  
yHat = regression.lwlrTest(xArr,xArr,yArr,0.5)    # 预测xArr,可以给不同的k测试不同的效果

# 绘制估计值和原始值
xMat = mat(xArr)
srtInd = xMat[:,1].argsort(0)
xSort = xMat[srtInd][:,0,:]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:,1],yHat[srtInd])
ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
plt.show()


# 在真实数据上
reload(regression)
abX,abY = regression.loadDataSet('abalone.txt')
yHat01 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
yHat1 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
yHat10 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)
# 看下k取什么比较好，所谓的交叉验证也算是
regression.rssError(abY[0:99],yHat01.T)     # you are best~
regression.rssError(abY[0:99],yHat1.T)
regression.rssError(abY[0:99],yHat10.T)

# 看看是不是最好的k，测试集上也表现的良好
yHat01 = regression.lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
yHat1 = regression.lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
yHat10 = regression.lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)
regression.rssError(abY[100:199],yHat01.T)  # 明显过拟合了~
regression.rssError(abY[100:199],yHat1.T)
regression.rssError(abY[100:199],yHat10.T)  # You are really the best...有没有写错....


#　岭回归测试
reload(regression)
abX,abY = regression.loadDataSet('abalone.txt')
ridgeWeights = regression.ridgeTest(abX,abY)
# 绘制λ
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()


# lasso的测试
reload(regression)
xArr,yArr = regression.loadDataSet('abalone.txt')
regression.stageWise(xArr,yArr,0.01,200)
regression.stageWise(xArr,yArr,0.001,5000)


# 与最小二乘比较看下
xMat = mat(xArr)
yMat = mat(yArr).T
xMat = regression.regularize(xMat)
yM = mean(yMat,0)
yMat = yMat - yM
weights = regression.standRegres(xMat,yMat.T)
weights.T   # 返回的W应该差不多的


# 获取谷歌的数据
reload(regression)
lgX = []
lgY = []
regression.setDataCollect(lgX,lgY)


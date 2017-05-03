# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:52:37 2017

@author: kaifeng
"""

import kNN
import numpy as np

group , labels = kNN.creatDataSet()
# 调用函数获取数据

group
labels

pre = kNN.classify0([0,0],group,labels,3)
pre
# 预测[0,1]的分类

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
datingDataMat
datingLabels
# 调用文件处理函数，获取数据

# 分析数据
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
plt.show()


normMat,ranges,minVals = kNN.autoNorm(datingDataMat)
normMat
ranges
minVals
# 调用标准化函数，把数据集处理

#调用分类器
kNN.datingClassTest()


# 调用函数，把图像信息转化成向量 
tectVector = kNN.img2vector('testDights/0_13.txt')
tectVector

# 调用函数预测图像中出现的手写字
kNN.handwritingClassTest()













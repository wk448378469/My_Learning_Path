# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:26:16 2017

@author: 凯风
"""

import pca
from imp import reload
import numpy as np
import matplotlib.pyplot as plt


reload(pca)
dataMat = pca.loadDataSet('testSet.txt')    # 读取数据，这个数据集是二维的
lowDMat,reconMat = pca.pca(dataMat,1)       # 降维
np.shape(lowDMat)                           

# 画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=90)
ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=50,c='red')


# 在500维的数据上进行降维
reload(pca)
dataMat = pca.replaceNanWithMean()      # 获取处理后的数据
pca.createFig()     # 根据这个可以看到特征数量在20左右就覆盖了数据集的绝大部分的方差了，可以根据这个选择降维的参数
lowDMat,reconMat = pca.pca(dataMat,20)       # 降维


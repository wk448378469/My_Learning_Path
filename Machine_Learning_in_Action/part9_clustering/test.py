# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:57:07 2017

@author: 凯风
"""

import kMeans
import numpy as np
from imp import reload

reload(kMeans)
datMat = np.mat(kMeans.loadDataSet('testSet.txt'))
min(datMat[:,0])
max(datMat[:,0])
min(datMat[:,1])
max(datMat[:,1])
kMeans.randCent(datMat,2)   # 看一下初始化的质心是否在取值范围内
kMeans.distEclud(datMat[0],datMat[1])

# 在实际数据上看下K-means
reload(kMeans)
datMat = np.mat(kMeans.loadDataSet('testSet.txt'))
myCentroids,clustAssing = kMeans.kMeans(datMat,4)   # 不一定是全局最优解


# 二分k-means
reload(kMeans)
datMat3 = np.mat(kMeans.loadDataSet('testSet2.txt'))
centList,myNewAssments = kMeans.biKmeans(datMat3,3) # 其实依然无法保证全局最优解，只能是局部最优解
centList
myNewAssments

# 利用二分k-means在图上画出簇
reload(kMeans)
kMeans.clusterClubs(4)







             
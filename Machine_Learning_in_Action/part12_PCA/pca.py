# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:29:52 2017

@author: 凯风
"""

import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(fileName,delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [list(map(float,line)) for line in stringArr]
    return np.mat(datArr)

def pca(dataMat,topNfeat = 9999999):
    meanVals = np.mean(dataMat,axis=0)                  # 求特征的平均值
    meanRemoved = dataMat - meanVals                    # 减去平均值
    covMat = np.cov(meanRemoved,rowvar=0)               # 求协方差矩阵
    eigVals,eigVects = np.linalg.eig(np.mat(covMat))    # 求特征值和特征向量
    eigValInd = np.argsort(eigVals)                     # 对特征值排序，并得到对应索引值
    eigValInd = eigValInd[:-(topNfeat+1):-1]            # 对索引值降维
    redEigVects = eigVects[:,eigValInd]                 # 根据索引值得到对应的特征向量
    lowDDataMat = meanRemoved * redEigVects             # 将数据转换到新的空间,即去军之后的矩阵 * 特征向量 
    reconMat = (lowDDataMat * redEigVects.T) + meanVals     # 还原数据
    return lowDDataMat,reconMat


def replaceNanWithMean():
    datMat = loadDataSet('secom.data',' ')              # 获取数据
    numFeat = np.shape(datMat)[1]                       # 获取特征数
    for i in range(numFeat):
        meanVal = np.mean(datMat[np.nonzero(~np.isnan(datMat[:,i].A))[0],i])    # 求平均值，并忽略每个特征中的缺失值
        datMat[np.nonzero(np.isnan(datMat[:,i].A))[0],i] = meanVal              # 缺失值用平均值所代替
    return datMat

def createFig():
    # 画图，主要是主成分数目和方差百分比的趋势图
    dataMat = replaceNanWithMean()  
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    covMat = np.cov(meanRemoved, rowvar=0)
    eigVals,eigVects = np.linalg.eig(np.mat(covMat))
    eigValInd = np.argsort(eigVals)
    eigValInd = eigValInd[::-1]
    sortedEigVals = eigVals[eigValInd]
    # 以上内容和PCA主函数差不多
    total = sum(sortedEigVals)      # 求方差的和
    varPercentage = sortedEigVals/total*100     # 计算每个特征的方差占比情况
    
    # 绘制图片
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(1, 21), varPercentage[:20], marker='^')
    plt.xlabel('Principal Component Number')
    plt.ylabel('Percentage of Variance')
    plt.show()
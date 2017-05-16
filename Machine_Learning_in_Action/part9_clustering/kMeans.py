# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:50:10 2017

@author: 凯风
"""

import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(filename):
    # 导入数据
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA,vecB):
    # 计算欧氏距离
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet,k):
    # 初始化质心，确定每个特征的最大值最小值后，在其区间内随机
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ*np.random.rand(k,1)
    return centroids    # kmean的特点，每次初始化的点不同进而产生不同的质心

def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    # 核心算法，接受数据集和要求的几个质心，后两个参数可能之后有不同的方法
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))    # 干嘛de...应该是存放每个样本被分到哪个簇去了，第二列存放误差（就是距离拉）
    centroids = createCent(dataSet,k)           # 初始化质心
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1       # 初始化属于哪个簇的变量
            for j in range(k):  # 对于每个样本寻找距离最近的质心
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex:     # 退出条件，是从从一个簇变到了另一个
                clusterChanged =True
            clusterAssment[i,:] = minIndex,minDist**2
        print (centroids)
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = np.mean(ptsInClust,axis=0)      # 更新质心的位置
    return centroids,clusterAssment     # 返回质心的坐标以及样本的质心分配结果及到对应质心的距离


def biKmeans(dataSet , k , distMeas = distEclud):
    # 二分Kmeans
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))    # 和之前一样
    centroid0 = np.mean(dataSet,axis=0).tolist()[0]
    centList = [centroid0]      # 初始化一个簇来保存质心
    for j in range(m):
        # 计算每个样本的距离
        clusterAssment[j,1] = distMeas(np.mat(centroid0) , dataSet[j,:]) ** 2
    while len(centList) < k:
        lowestSSE = np.inf
        for i in range(len(centList)):
            # 尝试划分每一个簇
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:,0].A == i)[0],:]
            centroidMat,splitClustAss = kMeans(ptsInCurrCluster,2,distMeas) # 二分
            sseSplit = np.sum(splitClustAss[:,1])
            sseNotSplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:,0].A != i)[0],1])
            print ('sseSplit and not notSplit:',sseSplit,sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) # 更新簇的分配结果
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentSplit
        print ('the best center to split is:',bestCentSplit)
        print ('the len of best clustass is:',len(bestClustAss))
        centList[bestCentSplit] = bestNewCents[0,:].tolist()[0]
        centList.append(bestNewCents[1,:].tolist()[0])
        clusterAssment[np.nonzero(clusterAssment[:,0].A == bestCentSplit)[0],:] = bestClustAss
    return np.mat(centList) , clusterAssment

def geoGrab():
    #这两个是通过雅虎API获取数据的，上节课获取google的就比较难，所以这次先算了
    pass
def massPlaceFind(fileName):
    pass

def distSLC(vecA,vecB):
    # 根据经纬度计算两个点的距离
    a = np.sin(vecA[0,1] * np.pi/180) * np.sin(vecB[0,1]*np.pi/180)
    b = np.cos(vecA[0,1] * np.pi/180) * np.cos(vecB[0,1]*np.pi/180)*np.cos(np.pi*(vecB[0,0] - vecA[0,0])/180)
    return np.arccos(a+b)*6371.0

def clusterClubs(numClust = 5):
    # 利用二分均值在图上画出簇中心
    datList = []
    for line in open('places.txt').readlines():
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]),float(lineArr[3])])
    datMat = np.mat(datList)
    myCentroids,clustAssing = biKmeans(datMat,numClust,distMeas=distSLC)
    fig = plt.figure()
    rect = [0.1,0.1,0.8,0.8]
    scatterMarkers = ['s','o','^','8','p','d','v','h','>','<']  # 存放一些标签，作为图例吧算是
    axprops = dict(xticks = [] , yticks = [])
    ax0 = fig.add_axes(rect,label='ax0',**axprops)
    imgP = plt.imread('Portland.png')
    ax0.imshow(imgP)
    ax1 = fig.add_axes(rect,label='ax1',frameon=False)
    for i in range(numClust):   # 画图ing
        ptsInCurrCluster = datMat[np.nonzero(clustAssing[:,0].A == i)[0],:]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0],
                    ptsInCurrCluster[:,1].flatten().A[0],
                    marker = markerStyle, s = 90)
    ax1.scatter(myCentroids[:,0].flatten().A[0],
                myCentroids[:,1].flatten().A[0],
                           marker = '+', s = 300)
    plt.show()
        
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:34:54 2017

@author: kaifeng
"""

import scipy as sp
import numpy as np

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(intX):
    '''
        sigmoid这个函数公式的计算
        或者叫做logistics函数
        hθ(x) = g(θ^T * x) = 1/(1+e^(-θ^T * x))
    '''
    return 1.0/(1+sp.exp(-intX))


def gradAscent(dataMatIn,labelMatIn):
    # 批梯度下降
    dataMatrix = np.mat(dataMatIn)      # 转换成np的矩阵形式
    labelMat = np.mat(labelMatIn).transpose()       # transpose是转置
    m , n = np.shape(dataMatrix)                # 获取样本数和特征数
    alpha = 0.001                               # 梯度上升的更新系数
    maxCycles = 500                             # 最大迭代次数
    weights = np.ones((n,1))                    # 需要几个θ来拟合，三个特征就用三个，但是为啥要强加一个呢？
    for k in range(maxCycles):                  
        h = sigmoid(dataMatrix * weights)       # θX 给 logistics函数
        error = (labelMat-h)                    # 计算误差
        weights = weights + alpha*dataMatrix.transpose()*error      # θ更新公式
    return weights

def stocGradAscent(dataMatrix,classLabels):
    # 随机梯度下降,每次选取一个样本来更新参数θ
    m,n = np.shape(dataMatrix)
    alpha = 0.01
    weights = np.ones(n)
    for i in range(m):
        h = sigmoid(dataMatrix[i]*weights)
        error = classLabels[i] - h
        weights = weights + alpha*error*dataMatrix[i]
    return weights

def stocGradAscentNew(dataMatrix,classLabels,numIter=150):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i) + 0.01      # 学习速度每次都调整
            randIndex = int(np.random.uniform(0,len(dataIndex)))    # 随机选取样本
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha*error*dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat = loadDataSet()            # 读取数据
    dataArr = np.array(dataMat)                 # 转成数组
    n = np.shape(dataArr)[0]                    # 获取样本数
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x = np.arange(-3.0 , 3.0 , 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]       # 拟合最优解，此处hθ(x) = 0,X0=1,求解X1和X2的关系式
    ax.plot(x,y.transpose())
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def classifyVector(inX,weights):
    # 分类函数
    prob = sigmoid(sum(inX*weights))
    if prob>0.5:
        return 1.0
    else:
        return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    # 这两个文件均已完成预处理了
    '''
        缺失值的处理方法如下：
            1、用该特征的均值来填充缺失值
            2、使用特殊值来填充缺失值，如-1、0（这次是用0，因为不影响参数更新和logistics函数预测）
            3、忽略有缺失的样本
            4、使用类似的样本的均值添补缺失值
            5、使用另外的机器学习算法来预测缺失值
    '''
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscentNew(np.array(trainingSet),trainingLabels,500)
    errorCount = 0
    numTestVect = 0.0
    for line in frTest.readlines():
        numTestVect += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(np.array(lineArr),trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVect)
    print ('the error rate of this test is : %f' %errorRate)
    return errorRate

def multiTest():
    numTest = 10
    errorSum = 0.0
    for k in range(numTest):
        errorSum += colicTest()
    print ('final average error rate is ',errorSum/float(numTest))








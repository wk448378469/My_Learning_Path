# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:27:13 2017

@author: 凯风
"""

from numpy import *
from time import sleep
import json
import urllib
# 实在懒得每个方法前面加np了....

def loadDataSet(filename):
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat


def standRegres(xArr,yArr):
    # 矩阵法求回归系数
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:      # 计算行列式，若为0则没办法求出逆矩阵
        print ('this matrix is singular,cannot do inverse')
        return
    ws = xTx.I * (xMat.T * yMat)    # w = ((X^T * X)^-1)*X^T*y
    return ws


def lwlr(testPoint,xArr,yArr,k=1.0):
    # 局部加权线性回归
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))     # 创建一个对角矩阵(除对角线外均是0)
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))   # 利用“高斯核”来求加权
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print ('this matrix is singular , cannot do inverse')
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint*ws

def lwlrTest(testPoint,xArr,yArr,k=1.0):
    m = shape(testPoint)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testPoint[i],xArr,yArr,k)
    return yHat

def rssError(yArr,yHatArr):
    # 这叫什么来着，误差吧就算
    return ((yArr-yHatArr)**2).sum()


def ridgeRegres(xMat,yMat,lam=0.2):
    # 岭回归，主要解决n>m的问题，主要思想就是在矩阵X^T * X上加入一个λI，从而可求逆矩阵
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0:
        print ('this matrix is singular , cannot do inverse')
        return
    ws = denom.I * (xMat.T * yMat)
    return ws

def ridgeTest(xArr,yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    #标准化，减去均值，除以方差
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMean = mean(xMat,0)
    xVar = var(xMat,0)
    xMat = (xMat - xMean)/xVar
    numTestPts = 30         # 30个λ，用来区分不同的当λ下的效果，当λ=0时，和线性回归差不多了就
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat,yMat,exp(i-10))
        wMat[i,:] = ws.T
    return wMat


def regularize(xMat):
    # 标准化函数
    inMat = xMat.copy()
    inMeans = mean(inMat,0)
    inVar = var(inMat,0)
    inMat = (inMat - inMeans)/inVar
    return inMat

def stageWise(xArr,yArr,eps=0.01,numIt=100):
    # lasso 的简化版本(前向逐步回归)，eps最小迭代步长，numIt迭代次数
    xMat = mat(xArr)
    yMat = mat(yArr).T
    # 标准化
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m,n = shape(xMat)
    # 返回矩阵设定
    returnMat = zeros((numIt,n))
    ws = zeros((n,1))
    wsTest = ws.copy()  # w的备份
    wsMax = ws.copy()   # w的备份
    for i in range(numIt):
        print (ws.T)
        lowestError = inf
        for j in range(n):      # 在所有特征上迭代两次，分别增加和减少一个特征看对误差的影响
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] += eps*sign   # 更新第J个w
                yTest = xMat*wsTest
                rssE = rssError(yMat.A,yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:] = ws.T
    return returnMat



def searchForSet(retX,retY,setNum,yr,numPce,origPrc):
    # 貌似访问有些问题....
    sleep(10)
    myAPIstr = 'get from code.google.com'
    searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json' % (myAPIstr, setNum)
    pg = urllib.request.urlopen(searchURL)
    retDict = json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem = retDict['items'][i]
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else:
                newFlag =0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if sellingPrice > origPrc * 0.5:    # 过滤掉一些不完整的数据
                    print ('%d\t%d\t%d\t%f\t%f',(yr,numPce,newFlag,origPrc,sellingPrice))
                    retX.append([yr,numPce,newFlag,origPrc])
                    retY.append(sellingPrice)
        except:
            print ('problem with item',i)

def setDataCollect(retX,retY):
    # 调用searchForSet函数
    searchForSet(retX, retY, 8288, 2006, 800, 49.99)
    searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
    searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
    searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
    searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
    searchForSet(retX, retY, 10196, 2009, 3263, 249.99)


def crossValidation(xArr,yArr,numVal=10):
    # 交叉验证，默认10折
    m = len(yArr)
    indexList = list(range(m))
    errorMat = zeros((numVal,30))   # 创建一个错误集
    for i in range(numVal):
        # 创建训练集和测试集
        trainX = []
        trainY = []
        testX = []
        testY = []
        random.shuffle(indexList)       # 把indexList的位置混洗
        for j in range(m):
            # 划分数据集
            if j < m*0.9:
                trainX.append(xArr[indexList[j]])
                trainY.append(yArr[indexList[j]])
            else:
                testX.append(xArr[indexList[j]])
                testY.append(yArr[indexList[j]])
        wMat = ridgeTest(trainX,trainY)
        for k in range(30):
            matTestX = mat(testX)
            matTrainX = mat(trainX)
            meanTrain = mean(matTrainX,0)
            varTrain = var(matTrainX,0)     # 把测试数据也标准化
            matTestX = (matTestX - meanTrain)/varTrain
            yEst = matTestX * mat(wMat[k,:]).T + mean(trainY)
            errorMat[i,k] = rssError(yEst.T.A , array(testY))
    meanErrors = mean(errorMat,0)   
    minMean = float(min(meanErrors))
    bestWeights = wMat[nonzero(meanErrors == minMean)]
    xMat = mat(xArr)
    yMat = mat(yArr).T
    meanX = mean(xMat,0)
    varX = var(xMat,0)
    unReg = bestWeights/varX
    print ('the best model from ridge regreesion is :',unReg)
    print ('with constant term:',(-1*sum(multiply(meanX,unReg))+mean(yMat)))    # 数据还原
    
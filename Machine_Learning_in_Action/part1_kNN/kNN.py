# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:54:58 2017

@author: kaifeng
"""

from numpy import *
import operator         #运算符模块
from os import listdir

def creatDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]                      # 获取数据的已知数据的行数
    diffMat = tile(inX,(dataSetSize,1)) - dataSet       # 把inX变成和dataset一样的shape后，每个分量减去dataset
    sqDiffMat = diffMat ** 2                           # 计算平方
    sqDistances = sqDiffMat.sum(axis=1)                  # 求和
    distances = sqDistances ** 0.5                        # 开平方
    # 计算已知类别数据集中的点与当前点的距离
    
    sortedDistIndicies = distances.argsort()
    # 获取个数组用来存放distances大小排序的
    
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # 选取K个与当前距离最小的k个点

    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    # 排序
    
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)        # 获取行数
            
    returnMat = zeros((numberOfLines,3))    # 生产一个全是0的，和行数一样的，3列的矩阵
    classLabelVector = []                   # 空的标签列表
    index = 0
    for line in arrayOLines:
        line = line.strip()                 # 删除空白符
        listFromLine = line.split('\t')             # 以\t为分隔符分割每一行
        returnMat[index,:] = listFromLine[0:3]           #把分割后的元素给returnMax
        classLabelVector.append(int(listFromLine[-1]))      # 把最后一列的元素给classLabelVector
        index += 1
    return returnMat,classLabelVector
    
    
def autoNorm(dataSet):
    minVals = dataSet.min(0)           # 每一列的最小值，是(1,3)
    maxVals = dataSet.max(0)            # 每一列的最大值，是(1,3)
    ranges = maxVals-minVals              # 每一列的范围值
    normDataSet = zeros(shape(dataSet))          # 创建一个新的要返回的，shape和dataSet一致
    m = dataSet.shape[0]                        # dataSet的行数
    normDataSet = dataSet - tile(minVals,(m,1))     # 每个元素减去对应列的最小值
    normDataSet = normDataSet/tile(ranges,(m,1))    # 每个元素除以对应列的范围值
    return normDataSet,ranges,minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat , ranges , minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ('the classifier came back with %d , the real answer is : %d' % (classifierResult,datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print ('the total error rate is :' , errorCount/float(numTestVecs))
    


def img2vector(filename):
    returnVect = zeros((1,1024))         # 生成一个要返回的向量，因为32*32=1024
    fr = open(filename)
    for i in range(32):                 # i控制列向下
        lineStr = fr.readline()
        for j in range(32):             # j控制行向前
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect



def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #读取整个文件夹中的内容
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #去掉.txt
        classNumStr = int(fileStr.split('_')[0])    #去掉_后面的
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        # 读取测试集
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 2)
        print ('the classifier cameback with %d,the real answer is : %d' % (classifierResult,classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print ('\n the total number of error is :',errorCount)
    print ('\n the total error rare is :',(errorCount/float(mTest)))
    # 我擦整个错误率。。。。。。。。











    
